#!/usr/bin/env python

"""
Description:
a script to manage a collection of git repositories,
with one folder per student

\b
Config files:
00.ids: where to store the students ids (and optionally reponames)
00.reponame (optional): how the student repo is supposed to be named

\b
Workflow:
1. ask each student to create a github repo named like e.g. numerique-homework
   they make sure you can read it (usually private + collaborator)
   beware to accept their invitation in a timely manner, as a github
   invitation expires after typically 7 days
2. you - the teacher - create a fresh folder, named after the target reponame
   so typically you would create a folder named numerique-homework too
   (alternately, if this convention does not suit you, you can instead
   create a file named `00.reponame` containing the name of the students repos
   e.g. numerique-homework)
   this will be used to locate the student repos to be cloned
3. in that folder you create a file `00.ids` containing the github slugs (ids) of the students
   all the ones that you are aware of at least
4. run this script to clone all the repos with
   collect-homework clone
5. as you receive new invitations:
   - add them to 00.ids if missing
   - re-run the clone command - which is idempotent
     i.e. can be done several times, existing folders will be skipped
     so only the missing students are tried again
6. if a student has misspelled their repo name
   e.g. their repo is called homework-num instead of the expected numerique-homework
   then tweak 00.ids to reflect this (see the format below)
7. iterate until you have all the slugs and all the repos cloned
8. from then on, use fetch / pull to update all the repos
   and all the other commands to check the status, diffs, logs, etc
9. of particular interest is the summary command, try it out

\b
Focusing on a subset of students:
you can use the -s option to restrict to one or several students, like so

  collect-homework -s "bobarteam" -s "john/,albert" summary

\b
Format for 00.ids:
00.ids is supposed to contain, one per line, the github ids of the students
it can contain comments, starting with a #
for each student you can use any of the following formats
 - https://github.com/student/repo
 - student/repo
 - student

when the repo is not provided, it is assumed to be
  either the content of 00.reponame if that file exists
  otherwise the name of the current folder
"""

import sys
import os
from pathlib import Path
import re
import subprocess

import click

from collect_homework.parallel_shells import ParallelShells


CFG_REPONAME = "00.reponame"
CFG_SLUGS = "00.ids"

# globals
SLUGS = {}      # dict of slug -> reponame
DIRS = []       # list of actual directories present
REPONAME = ""   # the default reponame


class Init:
    """
    reads current status
    """

    @staticmethod
    def get_reponame():
        cfg_reponame = Path(CFG_REPONAME)
        if not cfg_reponame.exists():
            return Path(".").absolute().parts[-1]
        with cfg_reponame.open() as f:
            return f.read().strip()

    @staticmethod
    def get_slugs(default_reponame):
        cfg_slugs = Path(CFG_SLUGS)
        result = {}
        with cfg_slugs.open() as f:
            for lineno, line in enumerate(f, 1):
                if line.startswith('#'):
                    continue
                line = line.strip()
                if not line:
                    continue
                if "/" in line:
                    try:
                        if line.endswith("/"):
                            line = line[:-1]
                        if line.endswith(".git"):
                            line = line[:-4]
                        line = line.replace("https://github.com/", "")
                        line = line.replace("git@github.com:", "")
                        slug, reponame = line.split("/")
                    except ValueError:
                        print(f"WARNING: ignoring line {lineno} with error", line)
                        continue
                else:
                    slug = line
                    reponame = default_reponame
                result[slug] = reponame
        return dict(sorted(result.items(), key=lambda x: x[0].lower()))

    @staticmethod
    def get_actual_repos():
        for dir in Path(".").glob("*/.git"):
            yield dir.parent.parts[-1]


# globals

def change_directory():
    """
    travel upwards until we find 00.ids
    otherwise stay in the current directory and issue a warning
    """
    global REPONAME, SLUGS, DIRS

    start = here = Path(".").absolute()
    while True:
        # found 00.ids
        if (here / CFG_SLUGS).exists():
            if start != here:
                print(f"WARNING: working from {here}")
                os.chdir(here)
            REPONAME = Init.get_reponame()
            SLUGS = Init.get_slugs(REPONAME)
            DIRS = list(Init.get_actual_repos())
            return
        # not find at all
        if here.parent == here:
            print(f"warning, config file {CFG_SLUGS} not found")
            REPONAME = "unknown"
            SLUGS = {}
            DIRS = []
            return
        # otherwise go one level up and try again
        here = here.parent

change_directory()


def _git_proxy(message, *git_command):
    """
    Run a git command on all DIRS
    """
    for slug in Init.get_actual_repos():
        if slug not in SLUGS:
            continue
        if message:
            print(f"===== {message} in {slug}")
        command = ["git", "-C", slug, *git_command]
        # print(command)
        subprocess.run(command)

# message not used yet
def _git_proxy_parallel(_message, *git_command):
    """
    Run a git command on all DIRS, but asynchronously
    """
    commands = []
    for slug in Init.get_actual_repos():
        if slug not in SLUGS:
            continue
        command = f"git -C {slug} {' '.join(git_command)}"
        commands.append(command)
    ParallelShells(commands).run()

# the click CLI object
@click.group(chain=True, help=sys.modules[__name__].__doc__)
@click.option('-s', '--students', multiple=True, help="comma-separated, cumulative")
def cli(students):
    # being multiple, we receive a tuple of strings
    if not students:
        return
    global SLUGS
    focus_slugs = {}
    # allow either comma, space or slash as separator in each -s option
    students = sum((re.split(r'[,\s]+', student) for student in students), [] )
    for student in students:
        if not student:
            continue
        if student not in SLUGS and Path(student).exists():
                student = Path(student).absolute().parts[-1]
                print(f"-> using slug {student}")
        if student not in SLUGS:
            print(f"unknown student {student} in {CFG_SLUGS}")
            exit(1)
        focus_slugs[student] = SLUGS[student]
    SLUGS = focus_slugs


# commands
@cli.command('slugs', help="show the slugs, optionally with reponames")
@click.option('-v', '--verbose', is_flag=True, default=False, help="show reponames", )
def slugs(verbose):
    for slug, reponame in SLUGS.items():
        print(f"{slug}/{reponame}" if verbose else slug)

@cli.command('dirs', help="show the repos currently present")
def dirs():
    for dir in sorted(DIRS, key=lambda x: x.lower()):
        print(dir)

@cli.command('missing', help="show the missing directories")
def missing():
    for slug, reponame in SLUGS.items():
        if slug not in DIRS:
            print(slug)

@cli.command('empty', help="show the empty directories")
def empty():
    for slug in DIRS:
        retcod = subprocess.run(f"git -C {slug} log --oneline >& /dev/null",
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                shell=True).returncode
        if retcod != 0:
            print(slug)

@cli.command('clone', help="clone all missing repos")
def clone():
    commands = []
    for slug, reponame in SLUGS.items():
        gitrepo = Path(slug) / ".git"
        if gitrepo.exists() and gitrepo.is_dir():
            print(f"{slug} -- already OK")
            continue
        commands.append(f"git clone git@github.com:{slug}/{reponame}.git {slug}")
    ParallelShells(commands).run()


@cli.command('urls', help="show the urls of the repos")
@click.option('-h', '--http', is_flag=True, default=False, help="show http urls")
def urls(http):
    if not http:
        _git_proxy("", "remote", "get-url", "origin")
    else:
        for slug, reponame in SLUGS.items():
            print(f"https://github.com/{slug}/{reponame}")

@cli.command('status', help="do a full git status on the repos")
def status(): _git_proxy("STATUS", "status")

@cli.command('s', help="short status: one-liner, no untracked")
def s(): _git_proxy("SHORT STATUS", "status", "--short", "--untracked-files=no")

# so we can pass any extra args to git diff
@cli.command(
    'diff',
    context_settings=dict(ignore_unknown_options=True),
    help="do a git diff on the repos - all extra args are passed to git diff",
)
@click.argument('extra_args', type=click.UNPROCESSED, nargs=-1)
def diff(extra_args): _git_proxy("DIFF", "diff", *extra_args)

@cli.command('pull', help="do a git pull on the repos")
def pull(): _git_proxy_parallel("PULL", "pull")

@cli.command('fetch', help="do a git fetch on the repos")
def fetch(): _git_proxy_parallel("FETCH", "fetch")

@cli.command('reset', help="do a git reset --hard on the repos")
def reset(): _git_proxy("RESET", "reset", "--hard")

@cli.command('merge', help="do a git merge origin/main on the repos")
def merge(): _git_proxy("MERGE", "merge", "origin/main")


FORMAT = """--format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(dim bold red)%an%C(reset) - %s%C(red)%d%C(reset)'"""

@cli.command('log1', help="show the last commit of each repo - default format")
def log1(): _git_proxy("last commit", "log", "-1")

@cli.command('l1', help="show the last commit of each repo, one-liner")
def l1(): _git_proxy("", "log", "-1", FORMAT )

@cli.command('l5', help="show the 5 latest commits of each repo, one-liner")
def l5(): _git_proxy( "LISTING 5 latest commits", "log", "--oneline", "--all", "--graph", "-5", FORMAT )

@cli.command('ln', help="show the n latest commits of each repo, one-liner")
@click.argument('n', type=int)
def ln(n): _git_proxy( f"LISTING {n} latest commits", "log", "--oneline", "--all", "--graph", f"-{n}", FORMAT )


@cli.command('ls', context_settings=dict(ignore_unknown_options=True), help="runs git ls-files in the repos")
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def ls(args):
    args_str = ' '.join(args)
    _git_proxy(f"git ls-files {args_str}", "ls-files", *args)

@cli.command('raw', context_settings=dict(ignore_unknown_options=True), help="runs git what-you-want in the repos")
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def raw(args):
    if len(args) == 0:
        print("error: expecting at least one argument, the git subcommand")
        exit(1)
    args_str = ' '.join(args)
    _git_proxy(f"git {args_str}", *args)


# pour a bit of shell in the mix
summary_function = """
function summary() {
    local quiet="$1"; shift
    local verbose="$1"; shift
    local folder="$1"; shift
    local slug="$1"; shift
    # missing repo
    [[ -d $slug ]] || {
        [[ -z "$quiet" ]] && printf '%24s' $slug; echo '   --- MISSING ---'
        return 2
    }
    # empty repo
    git -C $slug log >& /dev/null || {
        [[ -z "$quiet" ]] && printf '%24s' $slug; echo '   --- EMPTY ---'
        return 1
    }
    printf '%24s ' $slug

    # folders
    local nb_git_folders=$(git -C $slug ls-tree -r --name-only HEAD \
        | awk -F/ 'NF>1{ p=$1; print p; for(i=2;i<NF;i++){ p=p"/"$i; print p }}' \
        | sort -u \
        | (cat -; echo .) \
        | wc -l
    )
    local nb_folders
    [[ -n "$verbose" ]] && nb_folders=$(find $slug -type d | grep -vE '/.git($|/)' | wc -l)

    # files
    local nb_git_files=$(git -C $slug ls-files | wc -l)
    local nb_files
    [[ -n "$verbose" ]] && nb_files=$(find $slug -type f | fgrep -v '/.git/' | wc -l)

    # commits
    local nb_commits=$(git -C $slug log --oneline | wc -l)
    local nb_commits_folder
    [[ -n "$folder" ]] && nb_commits_folder=$(git -C $slug log --oneline -- $folder | wc -l)

    # date
    local folder_opt=""
    [[ -n "$folder" ]] && folder_opt=" -- $folder"
    local dateh=$(git -C $slug log -1 --format='%ah' $folder_opt)
    local date=$(git -C $slug log -1 --format='%ar' $folder_opt)

    # output - commits
    printf "%3d" $nb_commits
    [[ -n "$folder" ]] && printf " (%3d for $folder)" $nb_commits_folder
    printf " commits - "

    # output - folders
    printf "%3d g" $nb_git_folders
    if [[ -n "$verbose" ]]; then
        [[ "$nb_git_folders" != "$nb_folders" ]] && printf " (%d wd)" $nb_folders
    fi
    printf " folders - "

    # output - files
    printf "%3d g" $nb_git_files
    if [[ -n "$verbose" ]]; then
        [[ "$nb_git_files" != "$nb_files" ]] && printf " (%d wd)" $nb_files
    fi
    printf " files - "

    # output - date
    if [[ -n "$verbose" ]]; then
        printf "last on %s (%s)" "$dateh" "$date"
    else
        printf "last %s" "$date"
    fi
    echo
    return 0
}
"""

@cli.command('summary', help="show a summary of the repos - counts commits touching folder if provided")
@click.option('-q', '--quiet', is_flag=True, default=False, help="silent missing repos")
@click.option('-v', '--verbose', is_flag=True, default=False, help="verbose mode")
@click.argument('folder', required=False)
def summary(quiet, verbose, folder):
    # translate into shell-friendly
    # bool -> "" or "non-empty"
    quiet = "quiet" if quiet else ""
    verbose = "verbose" if verbose else ""
    # None -> ""
    folder = folder or ""
    commands = []
    for slug, _ in SLUGS.items():
        commands.append(summary_function + f"summary '{quiet}' '{verbose}' '{folder}' {slug}")
    retcods = ParallelShells(commands, echo=False).run()
    total = len(SLUGS)
    message = f"total {total}"
    ok = sum(1 for r in retcods if r == 0)
    if ok:
        message += f", {ok} OK"
    missing = sum(1 for r in retcods if r == 2)
    if missing:
        message += f", {missing} missing"
    empty = sum(1 for r in retcods if r == 1)
    if empty:
        message += f", {empty} empty"
    print(message)
