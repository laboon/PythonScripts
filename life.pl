# This implements Conway's Game of Life in perl.

package Laboon_life;

use strict;
use warnings;

use constant ALIVE => 1;
use constant DEAD => 0;

use constant FALSE => 0;
use constant TRUE => 1;

our @board;
our $xSize;
our $ySize;

our $deadChar = '.';
our $liveChar = 'X';

sub stripWhitespace {
    my $toReturn = shift;
    $toReturn =~ s/^\s+//;
    $toReturn =~ s/\s+$//;
    return $toReturn;
}

sub readPosInt {
    my $prompt = shift;
    my $retVal = -1;
    my $readVal;
    print $prompt;
    while ($retVal < 0) {
        chomp($readVal = <STDIN>);
        if ($readVal =~ /^\d+$/) {
            if ($readVal eq "0") {
                print STDERR "Must be a positive integer.";
            } else {
                $retVal = $readVal;
            }
        } else {
            print STDERR "Must be a positive integer.";
        }
    }
    return $retVal;
}

sub setCell {
    my $x = shift;
    my $y = shift;
    my $curVal = $board[$x][$y];
    print "Setting cell @ $x $y (curVal = $curVal)...\n";
    if ($curVal == DEAD) {
        $board[$x][$y] = ALIVE;
    } elsif ($curVal == ALIVE) {
        $board[$x][$y] = DEAD;
    } else {
        die("Integrity error $x, $y = $curVal");
    }
}

sub getCell {
    my $x = shift;
    my $y = shift;
    # print "\t\tChecking $x $y..";
    if ($x < 0 || $y < 0 || $x >= $xSize || $y >= $ySize) {
        
        return DEAD;
    } else {
        
        return $board[$x][$y];
    }
}

sub getNumNeighborsAlive {
    my $x = shift;
    my $y = shift;
    my $count = 0;
    if (getCell($x - 1, $y - 1) == ALIVE) { $count ++; }
    if (getCell($x - 1, $y)     == ALIVE) { $count ++; }
    if (getCell($x - 1, $y + 1) == ALIVE) { $count ++; }
    if (getCell($x, $y - 1)     == ALIVE) { $count ++; }
    if (getCell($x, $y + 1)     == ALIVE) { $count ++; }
    if (getCell($x + 1, $y - 1) == ALIVE) { $count ++; }
    if (getCell($x + 1, $y)     == ALIVE) { $count ++; }
    if (getCell($x + 1, $y + 1) == ALIVE) { $count ++; }
    
    return $count;
}

sub statusNextRound {
    # Rules -
    # Any live cell with fewer than two live neighbours dies.
    # Any live cell with two or three live neighbours lives on.
    # Any live cell with more than three live neighbours dies.
    # Any dead cell with exactly three live neighbours becomes a live cell.
    my $x = shift;
    my $y = shift;
    my $currentState = getCell($x, $y);
    my $numNeighbors = getNumNeighborsAlive($x, $y);
    
    if ($currentState == ALIVE) {
        if ($numNeighbors < 2 || $numNeighbors > 3) {
            return DEAD;
        } else {
            return ALIVE;
        }
    }
    if ($currentState == DEAD) {
        if ($numNeighbors == 3) {
            return ALIVE;
        } else {
            return DEAD;
        }
    }
    
}

sub initBoard {
    my $x = shift;
    my $y = shift;
    $xSize = $x;
    $ySize = $y;
    my @tmp;
    for my $j (0 .. ($x - 1)) {
        for my $k (0 .. ($y - 1)) {
            push @tmp, DEAD;
        }
        push @board, [ @tmp ];
    }
}

sub printBoard {
    my $tmp;
    for my $j (0 .. ($xSize - 1)) {
        for my $k (0 .. ($ySize - 1)) {
            $tmp = $board[$j][$k];
            if ($tmp == 0) {
                print $deadChar;
            } else {
                print $liveChar;
            }
        }
        print "\n";
    }
}

sub setRandom {
    my $percent = shift;
    my $randNum = 0;
    for my $j (0 .. ($xSize -1)) {
        for my $k (0 .. ($ySize -1 )) {
            $randNum = int(rand(100));
            if ($randNum <= $percent) {
                setCell($j, $k);
            }
        }
    }
}

sub initCells {
    my @cells;
    my @coords;
    
    print "Either type a percentage to toggle, or enter specific cells to toggle in the format x,y;\n";
    my $tmpInput = <STDIN>;
    chomp $tmpInput;
    $tmpInput = stripWhitespace($tmpInput);
    if ($tmpInput =~ /%/) {
        # Get the percentage value, everything before the percentage sign
        setRandom(substr($tmpInput, 0, index($tmpInput, '%')));
    } else {
        @cells = split(/;/, $tmpInput);
        print @cells;
        for my $oneCell (@cells) {
            
            if ($oneCell =~ /,/) {
                @coords = split(/,/, $oneCell);
                setCell($coords[0], $coords[1]);
            } else {
                # ignore
            }
        }
    }
}

sub setupBoard {
    my $x, my $y;
    $x = readPosInt("Size of x axis > ");
    $y = readPosInt("Size of y axis > ");
    initBoard($x, $y);
    initCells();
}

sub printHelp() {
    print "Perl Life Commands\n";
    print "? - Print this help text\n";
    print "n - /N/ext iteration\n";
    print "r - /R/un\n";
    print "q - /Q/uit\n";
    print "s - /S/ave state to file (NOT IMPLEMENTED!)\n";
    print "l - /L/oad state from file (NOT IMPLEMENTED!)\n";
    print "<positive integer> - Run this number of iterations\n";
}

# This is really, really, really suboptimal.  I should do this in
# a way that doesn't involve copying an array twice (!).

sub iterate {
    
    my @boardCopy;
    
    # Make a copy (initially all DEAD's, but it doesn't really matter)
    my @tmp;
    for my $j (0 .. ($xSize - 1)) {
        for my $k (0 .. ($ySize - 1)) {
            push @tmp, DEAD;
        }
        push @boardCopy, [ @tmp ];
    }
    
    # Run the iterations on the copy based on data in original
    my $tmpStatus;
    for my $j (0 .. ($xSize - 1)) {
        for my $k (0 .. ($ySize - 1)) {
            $tmpStatus = statusNextRound($j, $k);
            $boardCopy[$j][$k] = $tmpStatus;
        }
    }
    
    # Move the copy back over
    for my $j (0 .. ($xSize - 1)) {
        for my $k (0 .. ($ySize - 1)) {
            $board[$j][$k] = $boardCopy[$j][$k];
        }
    }
    
}

sub saveToFile {
    # TODO
}

sub loadFromFile {
    # TODO
}

sub run() {
    my $changed = TRUE;
    my $cont = TRUE;
    #  main loop 
    while ($cont) {
        if ($changed) {
            printBoard();
        }
        $changed = TRUE;
        print "Command (? for help) > ";
        chomp(my $tmpInput = <STDIN>);
        $tmpInput = lc($tmpInput);
        if ($tmpInput eq 'n') {
            iterate();
        } elsif ($tmpInput =~ /^\d+$/) {
            $tmpInput = int($tmpInput);
            for my $j (0 .. ($tmpInput - 1 )) {
                iterate();
            }
        } elsif ($tmpInput eq 's') {
            print "Save not yet implemented...\n";
        } elsif ($tmpInput eq 'l') {
            print "Load not yet implemented...\n";
        } elsif ($tmpInput eq 'r') {
            while (TRUE) {
                iterate();
                printBoard();
            }
        } elsif ($tmpInput eq 'q') {
            $cont = FALSE;
        } elsif ($tmpInput eq '?') {
            $changed = FALSE;
            printHelp();
        } else {
            $changed = FALSE;
            print "Unknown command $tmpInput\n";
            printHelp();
        }
    }
    print "Exiting...\n";
}


# EXECUTION STARTS HERE
print "Laboon_life - an implementation of Conway's Game of Life\n";
setupBoard();
run();