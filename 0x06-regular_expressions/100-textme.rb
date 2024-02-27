#!/usr/bin/env ruby
puts ARGV[0].scan(/from:\K\+?\w+|to:\K\+?\w+|flags:\K[\-0-9:]*/).join(',')
