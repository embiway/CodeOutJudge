# $1 -> time limit
# $2 -> memory limit

# To do : Separately figure out if it is TLE or MLE.
# Figure out the exact time and memory taken by the programm

if [ $# != 2 ]
then
    echo -1
    exit 1
fi


g++ CodeExecutionEngine/curr_code.cpp -o tmp_exe


start=`date +%s.%N`
ulimit -t $1 -v $2; ./tmp_exe < CodeExecutionEngine/curr_input > tmp_output
end=`date +%s.%N`

runtime=$( echo "$end - $start" | bc -l )

if [[ ! (-s tmp_output) ]]
then
    echo 3 $1 $2
    rm tmp_exe tmp_output
    exit 1
fi

diff -w tmp_output CodeExecutionEngine/curr_expected_output > diff_res

if [ -s diff_res ]
then
    echo 0 $runtime $2
else
    echo 1 $runtime $2
fi

rm tmp_exe tmp_output