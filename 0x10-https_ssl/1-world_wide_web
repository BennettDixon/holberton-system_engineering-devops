#!/usr/bin/env bash
# script to report information about server domains
# shellcheck disable=SC2086
check_domain() {
	# awk will use record seperator of space
	# space sperated list of sub domains
	SUBDOMAINS='www lb-01 web-01 web-02'

	if [ -z "$1" ]; then
		exit
	fi
	# no sub domain specified, do all
	if [ -z "$2" ]; then
		echo "$SUBDOMAINS" | awk -v domain="$1"\
		'BEGIN { RS=" " }
		{split($0,ARR," ");
		cmd = "dig " ARR[1]"."domain " | grep -A1 \"ANSWER SECTION:\" | tail -n1";
		system(cmd)
		close(cmd)}' | awk\
		'{
		split($0, DOMS, ".");
		print "The subdomain " DOMS[1] " is a " $4 " record and points to " $5}'
	else
		dig "$2.$1" | grep -A1 "ANSWER SECTION:" | tail -n1 | awk\
		'{
		split($0, DOMS, ".");
		print "The subdomain " DOMS[1] " is a " $4 " record and points to " $5}'
	fi
}
check_domain "$1" "$2"
