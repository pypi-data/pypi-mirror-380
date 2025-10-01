#!/usr/bin/env python3

import os
import shlex
import subprocess
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from pathlib import Path
from tempfile import TemporaryDirectory

from contextlib import contextmanager
from typing import List, Union

# `--log-driver none` will prevent Docker from saving streamed data in logs,
# otherwise the storage on the remote disk fills up really fast.
DISABLE_DOCKER_LOGGING = '--log-driver none'
ALPINE_IMAGE = 'alpine:3.22.1'
RSYNC_IMAGE_NAME = 'rsync-image'
POSTGRES_IMAGE = 'postgres:18.0-alpine'
CWD = Path.cwd()
PROJECT_DEFAULT = CWD.name


def print_line(character: str):
    try:
        print(character * os.get_terminal_size()[0])
    except OSError:  # Not in a terminal
        print(character * 80)


def main():
    local_backup_root_dir = (CWD / 'backup').resolve()

    project_parser = ArgumentParser(add_help=False)
    project_parser.add_argument('--project', default=PROJECT_DEFAULT)
    project = project_parser.parse_known_args()[0].project

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(dest='action', required=True)
    clone_parser = subparsers.add_parser(
        'clone', formatter_class=ArgumentDefaultsHelpFormatter
    )
    backup_parser = subparsers.add_parser(
        'backup', formatter_class=ArgumentDefaultsHelpFormatter
    )
    restore_parser = subparsers.add_parser(
        'restore', formatter_class=ArgumentDefaultsHelpFormatter
    )

    for subparser in [clone_parser, backup_parser, restore_parser]:
        subparser.add_argument(
            '--project', default=PROJECT_DEFAULT, help='Docker Compose project name.'
        )
        subparser.add_argument(
            '--no-input', action='store_true', help='Say yes to all questions.'
        )
        subparser.add_argument(
            '--local-backup-dir',
            type=Path,
            default=local_backup_root_dir,
            help='Where the backup will be stored, on the machine running this script.',
        )
        subparser.add_argument(
            '--rsync-base-image',
            default=ALPINE_IMAGE,
            help='Base Docker image used for building the rsync image.',
        )
        subparser.add_argument(
            '--rsync-image',
            default=RSYNC_IMAGE_NAME,
            help='Name of the built Docker image for rsync.',
        )
        group = subparser.add_mutually_exclusive_group()
        group.add_argument(
            '--db-only', action='store_true', help='Apply only to the database.'
        )
        group.add_argument(
            '--media-only', action='store_true', help='Apply only to the media.'
        )

    db_socket_volume_default = f'{project}_postgresql-socket'
    media_volume_default = f'{project}_media'

    for subparser in [clone_parser, backup_parser]:
        subparser.add_argument(
            'source_ssh_address',
            nargs='?',
            help='Remote Docker host SSH address from which the data should be backed up, in the `username@host` or `host` form. Leave empty to use the local Docker instance.',
        )
        subparser.add_argument(
            '--source-db-image',
            default=POSTGRES_IMAGE,
            help='Name of the PostgreSQL image on the source machine.',
        )
        subparser.add_argument(
            '--source-db-socket-volume',
            default=db_socket_volume_default,
            help='Name of the Docker volume containing the PostgreSQL UNIX socket.',
        )
        subparser.add_argument(
            '--source-db-user', default=project, help='PostgreSQL user name.'
        )
        subparser.add_argument(
            '--source-db-database', default=project, help='PostgreSQL database name.'
        )
        subparser.add_argument(
            '--source-media-volume',
            default=media_volume_default,
            help='Docker volume name containing all the uploaded files of the website.',
        )

    for subparser in [clone_parser, restore_parser]:
        subparser.add_argument('--local-db-image', default=POSTGRES_IMAGE)
        subparser.add_argument(
            '--local-db-socket-volume',
            default=db_socket_volume_default,
            help='Name of the Docker volume containing the PostgreSQL UNIX socket.',
        )
        subparser.add_argument(
            '--local-db-user', default=project, help='PostgreSQL user name.'
        )
        subparser.add_argument(
            '--local-db-database', default=project, help='PostgreSQL database name.'
        )
        subparser.add_argument(
            '--local-media-volume',
            default=media_volume_default,
            help='Docker volume name containing all the uploaded files of the website.',
        )
        subparser.add_argument(
            '--local-media-user',
            default='django',
            help='Docker user of the media volume.',
        )

    args = parser.parse_args()

    no_input = args.no_input
    rsync_base_image = args.rsync_base_image
    rsync_dockerfile = f'FROM {rsync_base_image}\nRUN apk add rsync'
    rsync_image = args.rsync_image
    local_backup_dir = args.local_backup_dir
    local_backup_media_dir = local_backup_dir / 'media'
    local_backup_dump = local_backup_dir / 'db.dump'
    run_backup = args.action in {'clone', 'backup'}
    run_restore = args.action in {'clone', 'restore'}
    db_only = args.db_only
    media_only = args.media_only

    @contextmanager
    def tmp_rsync_dockerfile():
        with TemporaryDirectory() as tmp:
            with open(Path(tmp) / 'Dockerfile', 'w') as f:
                f.write(rsync_dockerfile)
            yield tmp

    def run(args: Union[List[str], str], **kwargs):
        print_line('=')
        prefix = ' '.join(
            [
                f'{k}={shlex.quote(v)}'
                for k, v in kwargs.get('env', {}).items()
                if os.environ.get(k) != v
            ]
        )
        command = (
            ' '.join([shlex.quote(str(arg)) for arg in args])
            if isinstance(args, list)
            else args
        )
        print(f'{prefix} {command}' if prefix else command)
        if not no_input and input('Run the above command? [yN] ').lower() != 'y':
            sys.exit(1)
        print_line('-')
        subprocess.run(args, check=True, **kwargs)
        print_line('=')
        print()

    if run_backup:
        source_ssh_address = args.source_ssh_address
        source_docker_host = f'ssh://{source_ssh_address}' if source_ssh_address else ''
        source_db_image = args.source_db_image
        source_db_socket_volume = args.source_db_socket_volume
        source_db_user = args.source_db_user
        source_db_database = args.source_db_database
        source_media_volume = args.source_media_volume

        def run_remote_docker(*args, **kwargs):
            env = {**os.environ}
            if source_docker_host:
                env['DOCKER_HOST'] = source_docker_host
            run(*args, **kwargs, env=env)

        print(f'Backing up data into {local_backup_dir!r}…')
        run(['mkdir', '-p', local_backup_dir])

        if not media_only:
            source_socket_mount = f'{source_db_socket_volume}:/var/run/postgresql'
            run_remote_docker(
                f'docker run --read-only -v {source_socket_mount} --rm -i {DISABLE_DOCKER_LOGGING} '
                f'{source_db_image} pg_dump -U {source_db_user} '
                f'-Fc -b -v {source_db_database} '
                f'> {local_backup_dump}',
                shell=True,
            )

        if not db_only:
            with tmp_rsync_dockerfile() as tmp:
                run_remote_docker(
                    ['docker', 'build', '-t', rsync_image, tmp],
                    stdin=subprocess.DEVNULL,
                )
            run(
                [
                    'rsync',
                    '--rsync-path',
                    f'docker run --read-only -v {source_media_volume}:/data:ro --rm -i {DISABLE_DOCKER_LOGGING} '
                    f'{rsync_image} rsync',
                    '--archive',
                    '--compress',
                    '--xattrs',
                    '--delete',
                    '--progress',
                    '--no-motd',
                    f'{source_ssh_address}:/data/' if source_ssh_address else '/data/',
                    local_backup_media_dir,
                ],
            )

    if run_restore:
        local_db_image = args.local_db_image
        local_db_socket_volume = args.local_db_socket_volume
        local_db_user = args.local_db_user
        local_db_database = args.local_db_database
        local_media_volume = args.local_media_volume
        local_media_user = args.local_media_user

        print(f'Restoring data from {local_backup_dir!r}')
        if not media_only:
            local_socket_mount = f'{local_db_socket_volume}:/var/run/postgresql'
            run(
                [
                    'docker',
                    'run',
                    '--read-only',
                    '-v',
                    local_socket_mount,
                    '--rm',
                    '-i',
                    *DISABLE_DOCKER_LOGGING.split(' '),
                    local_db_image,
                    'psql',
                    '-U',
                    local_db_user,
                    '-d',
                    local_db_database,
                    '-c',
                    f"""
                    DROP SCHEMA public CASCADE;
                    CREATE SCHEMA public;
                    GRANT ALL ON SCHEMA public TO {local_db_user}, public;
                """,
                ]
            )
            run(
                f'docker run --read-only -v {local_socket_mount} --rm -i {DISABLE_DOCKER_LOGGING} '
                f'{local_db_image} '
                f'pg_restore -U {local_db_user} -d {local_db_database} --if-exists --clean --exit-on-error -Fc '
                f'< {local_backup_dump}',
                shell=True,
            )

        if not db_only:
            with tmp_rsync_dockerfile() as tmp:
                run(
                    ['docker', 'build', '-t', rsync_image, tmp],
                    stdin=subprocess.DEVNULL,
                )
            run(
                [
                    'docker',
                    'run',
                    '-v',
                    f'{local_backup_media_dir}:/backup',
                    '-v',
                    f'{local_media_volume}:/data',
                    '--rm',
                    *DISABLE_DOCKER_LOGGING.split(' '),
                    rsync_image,
                    'sh',
                    '-c',
                    f'adduser --disabled-password --gecos "" --no-create-home {local_media_user} '
                    f'&& rsync --chown {local_media_user}:{local_media_user} --chmod 775 '
                    '--archive --xattrs --delete /backup/ /data/',
                ]
            )


if __name__ == '__main__':
    main()
