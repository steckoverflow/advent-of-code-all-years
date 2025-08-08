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

print $i - 1;

