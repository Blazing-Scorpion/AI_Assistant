#!/usr/bin/env bash

sudo rm -rfv /Volumes/*/.Trashes &>/dev/null
sudo rm -rfv ~/.Trash &>/dev/null
sudo rm -rfv /private/var/log/asl/*.asl &>/dev/null
sudo rm -rfv /Library/Logs/DiagnosticReports/* &>/dev/null
sudo rm -rfv /Library/Logs/Adobe/* &>/dev/null
rm -rfv ~/Library/Containers/com.apple.mail/Data/Library/Logs/Mail/* &>/dev/null
rm -rfv ~/Library/Logs/CoreSimulator/* &>/dev/null
sudo rm -rfv ~/Library/Application\ Support/Adobe/Common/Media\ Cache\ Files/* &>/dev/null
rm -rfv ~/Music/iTunes/iTunes\ Media/Mobile\ Applications/* &>/dev/null
rm -rfv ~/Library/Developer/Xcode/DerivedData/* &>/dev/null
rm -rfv ~/Library/Developer/Xcode/Archives/* &>/dev/null
brew cleanup --force -s &>/dev/null
brew cask cleanup &>/dev/null
rm -rfv /Library/Caches/Homebrew/* &>/dev/null
brew tap --repair &>/dev/null
gem cleanup &>/dev/null
