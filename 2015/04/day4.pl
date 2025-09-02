use strict;
use warnings;
use Digest::MD5 qw(md5_hex);

my $input = "iwrupvqb";
my $hash = "";
my $i = 0;

until (substr($hash, 0, 5) eq "00000") {
        $hash = md5_hex($input . $i);
        $i++;
}

print "Part 1: ";
print $i - 1;

$hash = "";
$i = 0;

until (substr($hash, 0, 6) eq "000000") {
        $hash = md5_hex($input . $i);
        $i++;
}

print "\nPart 2: ";
print $i - 1;


