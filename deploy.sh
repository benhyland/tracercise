#!/bin/sh

# also need to create and chmod data and png files

scp -r ./cgi-bin/* root@bhyland.co.uk:/usr/lib/cgi-bin/
