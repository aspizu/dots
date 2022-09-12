#!/bin/sh
xrdb ~/.Xresources
nitrogen --restore
picom &
easyeffects --gapplication-service &
sxhkd &
#wmclockmon -bw -bl -12 &
polybar main &
exec shod -d -m mod4 </dev/null
