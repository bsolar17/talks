#!/bin/sh
# Generates the demo repositories for git-survival-kit.md.
#
# Usage: ./demo.sh DIR [SCENARIO...]
#
# DIR must not exist yet; to start over, generate into a new one. Without
# SCENARIO, all of them are generated. Each scenario is a repo DIR/SCENARIO,
# with its remote in DIR/SCENARIO-origin.git and Alice's clone in
# DIR/SCENARIO-alice where needed. Authors, dates, and so commit IDs, are the
# same on every run.
#
# Each scenario stops one step before the trouble, so the demo can show the
# command that causes it ("Trouble:"), then the way out.
#
# Scenarios:
#   graph         on feature/refund, started from v1.0; a pull request was
#                 merged into origin/master since, not fetched yet; no
#                 trouble, just finding out where you are, then catching up
#                 with git rebase origin/master
#   conflict      feature/currency conflicts with master in Invoice.java
#                 Trouble: git rebase master
#   mess          the same branches
#                 Trouble: git rebase master, then resolve the conflict by
#                 picking one side: git checkout --theirs src/Invoice.java,
#                 git add src/Invoice.java, git rebase --continue
#   rebase-i      on feature/refund, not pushed yet: "Add refund" has a typo,
#                 "Debug charges" must not be shared; no command causes it,
#                 it's found by reviewing before pushing: git log -p master..
#   reflog        on feature/export, never merged; master has 2 unpushed
#                 commits and Alice pushed to origin/master
#                 Trouble: git switch master, git branch -D feature/export,
#                 git fetch, git reset --hard origin/master
#   pull          one local commit on master; Alice pushed, not fetched yet
#                 Trouble: git pull, which refuses; then the hint's first
#                 suggestion: git config --global pull.rebase false, git pull
#
# Commands run live create commits with the current date: from there on,
# commit IDs differ from run to run.
#
# Run the demos with the neutral config written to DIR/gitconfig, so your own
# settings (aliases, conflict style, ...) don't change what git shows, and
# `git config --global` changes only that file:
#
#   export GIT_CONFIG_GLOBAL=DIR/gitconfig
set -eu

usage() {
    awk 'NR > 2 && /^set -eu/ { exit } NR > 2' "$0" | sed 's/^# \{0,1\}//' >&2
    exit 2
}

SCENARIOS='graph conflict mess rebase-i reflog pull'

[ $# -ge 1 ] || usage
case $1 in -*) usage ;; esac
if [ -e "$1" ]; then
    echo "$1 already exists; generate into a new directory" >&2
    exit 1
fi
target=$1
shift
for scenario in "$@"; do
    case " $(echo $SCENARIOS) " in
    *" $scenario "*) ;;
    *) echo "Unknown scenario: $scenario" >&2; exit 2 ;;
    esac
done
mkdir -p "$target"
DIR=$(cd "$target" && pwd)

# Generate with git's defaults, whatever the user's own config says
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
export GIT_EDITOR=true GIT_MERGE_AUTOEDIT=no

cat > "$DIR/gitconfig" <<'EOF'
[user]
	name = Me
	email = me@example.com
[init]
	defaultBranch = master
EOF

# --- Helpers -----------------------------------------------------------------

TIME=1790838000 # 2026-10-01 09:00 +0200

as() {
    export GIT_AUTHOR_NAME="$1" GIT_COMMITTER_NAME="$1"
    email="$(echo "$1" | tr 'A-Z' 'a-z')@example.com"
    export GIT_AUTHOR_EMAIL="$email" GIT_COMMITTER_EMAIL="$email"
}

# Every commit, merge and ref update happens ten minutes after the last one
tick() {
    TIME=$((TIME + 600))
    export GIT_AUTHOR_DATE="$TIME +0200" GIT_COMMITTER_DATE="$TIME +0200"
}

commit() {
    tick
    git add -A
    git commit -q -m "$1"
}

merge() {
    tick
    git merge -q --no-ff "$@"
}

# Applies a sed script to a file, the same way on BSD and GNU sed
edit() {
    sed "$2" "$1" > "$1.tmp"
    mv "$1.tmp" "$1"
}

# Inserts stdin before the last line of a file, i.e. its closing brace; unlike
# sed's i command, keeps the indentation on BSD sed
insert_before_end() {
    TEXT=$(cat) awk 'NR > 1 { print prev } { prev = $0 }
        END { print ENVIRON["TEXT"]; print prev }' "$1" > "$1.tmp"
    mv "$1.tmp" "$1"
}

# A new repo DIR/$1 with its remote DIR/$1-origin.git, holding the first commits
init_with_origin() {
    git init -q --bare -b master "$DIR/$1-origin.git"
    git clone -q "$DIR/$1-origin.git" "$DIR/$1" 2>/dev/null
    cd "$DIR/$1"
    project
    git push -q origin master
}

# Alice's clone of the remote of scenario $1
alice_clone() {
    git clone -q "$DIR/$1-origin.git" "$DIR/$1-alice"
}

# --- The Example Project -----------------------------------------------------

project() {
    mkdir -p src
    cat > src/Invoice.java <<'EOF'
public class Invoice {
    private final long cents;

    public Invoice(long cents) {
        this.cents = cents;
    }

    public long cents() {
        return cents;
    }

    public String formatTotal() {
        return String.format("%d.%02d", cents / 100, cents % 100);
    }
}
EOF
    as Alice
    commit 'Add invoice'
    cat > src/Payment.java <<'EOF'
public class Payment {
    public void charge(Invoice invoice) {
        System.out.println("Charging " + invoice.formatTotal());
    }
}
EOF
    commit 'Add payment'
}

# Alice renames the field; the format line conflicts with show_currency
rename_cents() {
    as Alice
    edit src/Invoice.java '
        s/long cents;/long totalCents;/
        s/this\.cents = /this.totalCents = /
        s/return cents;/return totalCents;/
        s/", cents \/ 100, cents % 100/", totalCents \/ 100, totalCents % 100/'
    commit 'Rename cents to totalCents'
}

show_currency() {
    as Me
    edit src/Invoice.java 's/"%d\.%02d"/"CHF %d.%02d"/'
    commit 'Show currency in totals'
}

add_refund() {
    as Me
    insert_before_end src/Payment.java <<'EOF'

    public void refund(Invoice invoice) {
        System.out.println("Refunding " + invoice.formatTotal());
    }
EOF
    commit 'Add refund'
}

log_refunds() {
    as Me
    edit src/Payment.java 's/System\.out\.println("Refunding "/System.err.println("Refunding "/'
    commit 'Log refunds to stderr'
}

add_discount() {
    as Alice
    insert_before_end src/Invoice.java <<'EOF'

    public Invoice discounted(int percent) {
        return new Invoice(cents() * (100 - percent) / 100);
    }
EOF
    commit 'Add discounts'
}

# --- Scenarios ---------------------------------------------------------------

# Alice's pull request $1 from branch $2, merged the way a platform does
merge_pr() {
    git switch -q master
    as Alice
    merge "$2" -m "Merge pull request #$1 from alice/$2"
    git branch -q -d "$2"
    git push -q origin master
}

scenario_graph() {
    init_with_origin graph
    alice_clone graph
    cd "$DIR/graph-alice"
    git switch -q -c feature/discount
    add_discount
    merge_pr 1 feature/discount
    git tag v1.0
    git push -q origin v1.0
    # I start from v1.0
    cd "$DIR/graph"
    git pull -q
    git switch -q -c feature/refund
    add_refund
    log_refunds
    # Then another pull request is merged; my clone hasn't fetched it yet
    cd "$DIR/graph-alice"
    git switch -q -c bugfix/negative
    edit src/Invoice.java 's/        this\.cents = cents;/        if (cents < 0) throw new IllegalArgumentException();\
&/'
    commit 'Reject negative totals'
    merge_pr 2 bugfix/negative
}

# A new repo DIR/$1 where my feature/currency and Alice's master both change
# the same line of Invoice.java
currency_vs_rename() {
    git init -q -b master "$DIR/$1"
    cd "$DIR/$1"
    project
    git switch -q -c feature/currency
    show_currency
    add_refund
    log_refunds
    git switch -q master
    rename_cents
    git switch -q feature/currency
}

scenario_conflict() {
    currency_vs_rename conflict
}

scenario_mess() {
    currency_vs_rename mess
}

scenario_reflog() {
    init_with_origin reflog
    alice_clone reflog
    cd "$DIR/reflog-alice"
    rename_cents
    git push -q origin master
    cd "$DIR/reflog"
    show_currency
    add_refund
    git switch -q -c feature/export
    printf 'public class Export {\n}\n' > src/Export.java
    commit 'Add export'
    insert_before_end src/Export.java <<'EOF'
    public String csv(Invoice invoice) {
        return invoice.cents() + "\n";
    }
EOF
    commit 'Export invoices as CSV'
}

scenario_rebase_i() {
    init_with_origin rebase-i
    git switch -q -c feature/refund
    as Me
    insert_before_end src/Payment.java <<'EOF'

    public void refund(Invoice invoice) {
        System.out.println("Refnding " + invoice.formatTotal());
    }
EOF
    commit 'Add refund'
    edit src/Payment.java 's/    public void charge(Invoice invoice) {/&\
        System.out.println("DEBUG cents: " + invoice.cents());/'
    commit 'Debug charges'
    cat > src/PaymentTest.java <<'EOF'
public class PaymentTest {
    public static void main(String[] args) {
        new Payment().refund(new Invoice(1250));
    }
}
EOF
    commit 'Add refund test'
}

scenario_pull() {
    init_with_origin pull
    alice_clone pull
    cd "$DIR/pull-alice"
    rename_cents
    git push -q origin master
    cd "$DIR/pull"
    add_refund
}

# --- Main --------------------------------------------------------------------

for scenario in ${*:-$SCENARIOS}; do
    (scenario_$(echo "$scenario" | tr - _))
    echo "$DIR/$scenario"
done
