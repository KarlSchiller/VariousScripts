#!/bin/bash

# List of optional arguments:
# a          all, do normal update, clean and additional update
# c          clean, do clean
# o          other, do normal and other updates
# -nothing-  do normal updates

# Good vibes
printf "\n"
fortune
printf "\n"

# Arguments ###################################################################
# if no command line arg given set UPDATEPARAM to "not given"
if [ -z $1 ]
then
	UPDATEPARAM="not given"
elif [ -n $1 ]
then
	# otherwise make first arg as UPDATEPARAM
	UPDATEPARAM=$1
fi

# normal updates ###############################################################

case $UPDATEPARAM in
	"not given" | "a")
		# Ask for root permission
		sudo echo

		# apt
		printf "apt-get update\n"
		sudo apt-get update
		printf "\napt-get dist-upgrade\n"
		sudo apt-get dist-upgrade -y
		# Eigentlich nicht nötig nach dist-upgrade
		# printf "\napt-get upgrade\n"
		# sudo apt-get upgrade -y

		# flatpak
		printf "\nflatpak update\n"
		flatpak update -y

		# snap
		printf "\nsnap refresh\n"
		sudo snap refresh
		# The number of revisions stored by the system is set with the refresh.retain
		# option: sudo snap set system refresh.retain=2 (number between 2 and 20)
		;;
	*)
esac

# Keep the System clean #######################################################

case $UPDATEPARAM in
	"c" | "a")
		# Ask for root permission
		sudo echo

		printf "apt-get autoremove\n"
		sudo apt-get autoremove -y      # --show-progress druckt zu viel
		printf "\napt-get autoclean\n"
		sudo apt-get autoclean

		# vim
		printf "\nRemove old vim backups and swap files\n"
		SWAPDIR="$HOME/.vim/swap"
		if [ "$(ls -A $SWAPDIR)" ]; then
			# swap folder is not empty
			find $SWAPDIR -type f -exec echo Remove file {} \;
			find $SWAPDIR -type f -exec rm {} \;
		fi
		BACKUPDIR="$HOME/.vim/backup"
		if [ "$(ls -A $BACKUPDIR)" ]; then
			# backup folder is not empty
			find $BACKUPDIR -type f -exec echo Remove file {} \;
			find $BACKUPDIR -type f -exec rm {} \;
		fi
		;;
	*)
esac

# other Updates, that are not that important ###################################

case $UPDATEPARAM in
	"o" | "a")
		# Anaconda
		printf "\nconda update anaconda\n"
		conda update -y anaconda  # Updates everything according to consistency

		# Tex Live
		printf "\ntlmgr update --self\n"
		# Updates tlmgr itself
		tlmgr update --self
		printf "\ntlmgr update --all --reinstall-forcibly-removed\n"
		# Updates all packages
		# Packages forcibly removed by the user are reinstalled
		tlmgr update --all --reinstall-forcibly-removed
		;;
	*)
esac
