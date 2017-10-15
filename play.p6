#!/usr/bin/env perl6
use File::Find;
my $list = find(dir => '/tmp/mp3s', type => 'file', name => /\.mp3$/);
loop {
	my $track = roll(1, $list.cache);
	say $track;
	run 'ls', '-al', $track;
}