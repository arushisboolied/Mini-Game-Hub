#!/usr/bin/bash
declare -A stats

echo -e " _     _____    _    ____  _____ ____  ____   ___    _    ____  ____  \n| |   | ____|  / \  |  _ \| ____|  _ \| __ ) / _ \  / \  |  _ \|  _ \ \n| |   |  _|   / _ \ | | | |  _| | |_) |  _ \| | | |/ _ \ | |_) | | | |\n| |___| |___ / ___ \| |_| | |___|  _ <| |_) | |_| / ___ \|  _ <| |_| |\n|_____|_____/_/   \_\____/|_____|_| \_\____/ \___/_/   \_\_| \_\____/ "


for ((i=0;i<$(($#-4));i++)); do 
    var=$((i+5))
    Games[$i]=${!var}
done

x=$(cut -d ',' -f1,4 $1 | sort | uniq -c|awk '{print $1,$2}'|tr ' ' ','|tr -d '\r')
y=$(cut -d ',' -f2,4 $1 | sort | uniq -c|awk '{print $1,$2}'|tr ' ' ','|tr -d '\r')
Users=$(cut -d ' ' -f1 $2)

let n=0
while read -r line ; do
    usr_lists[$n]=$line
    ((n++))
done<<< $Users
while IFS=',' read -r wins winner game ; do
    stats["$winner:$game:wins"]=$wins
done <<< $x

while IFS=',' read -r losses loser game ; do
    stats["$loser:$game:losses"]=$losses
done <<< $y

for ((i=0;i<n;i++)); do

    user=${usr_lists[$i]}
    Final_stats[$i]=''
    total_wins=0
    total_losses=0
    for game in ${Games[@]}; do

        if [[ ${stats["$user:$game:losses"]:-0} == 0 ]]; then
            ratio="1e999"
        else
            ratio=$(echo "scale=3;${stats["$user:$game:wins"]:-0}/${stats["$user:$game:losses"]}"|bc -l)
        fi

        Final_stats[$i]+=",${stats["$user:$game:wins"]:-0},${stats["$user:$game:losses"]:-0},$ratio"

        ((total_losses+=${stats["$user:$game:losses"]:-0}))
        ((total_wins+=${stats["$user:$game:wins"]:-0}))
    done

    if [[ $total_losses == 0 ]]; then
        total_ratio="1e999"
    else
        total_ratio=$(echo "scale=3;$total_wins/$total_losses"|bc -l)
    fi

    Final_stats[$i]="$user${Final_stats[$i]},$total_wins,$total_losses,$total_ratio"
done

criteria=$(($3))
game_criteria=$(($4-1))
actual_criteria=$(($game_criteria*3+$criteria+1))
Games[$(($#-4))]="Total"
echo ${Final_stats[@]}|tr ' ' '\n'|sort -t ',' -k${actual_criteria},${actual_criteria}rg -k1,1|awk -F',' 'BEGIN { OFS="," }
{
    for (i = 2; i <= NF; i++) {
        if ($i == "1e999") {
            $i = "Undefeatable"
        }
    }
    print
}'|awk -F ',' -v Games="${Games[*]}" '
BEGIN{
    max[1]=9
    n=split(Games,arr," ")
    for (i=1;i<=n;i++){
        maxh[i]=length(arr[i])
        if (maxh[i]<21) maxh[i]=21
    }

}

NR==1{
    for (i=2;i<=NF;i++){
            if (i%3==0) max[i]=6
            if (i%3==1) max[i]=5
            if (i%3==2) max[i]=4
        }
}
{   
    table_data[NR,1]=$1
    if (length($1)>max[1]) max[1]=length($1)

    for (i=2;i<=NF;i++){
        table_data[NR,i]=$i
        if (length($i)>max[i]) max[i]=length($i)
    }

    cols=NF
    rows=NR
}
function stars(n,i){
    i=0
    s=""
    for (i=0;i<n;i++) s=s "-"
    return s
}
END{

    for (i=1;i<=n;i++){
        width=max[i*3-1]+max[i*3]+max[1+i*3]+6
        if (maxh[i]<width) maxh[i]=width      
    }

    printf "%s", "+" stars(max[1]+2)

    for (i=1;i<=n;i++){
        printf "+" stars(maxh[i]+2)
    }

    print "+"
    printf "| %-*s ", max[1], "Usernames"

    
    for (i=1;i<=n;i++){
        printf "| %-*s ", maxh[i], arr[i]     
    }

    print("|")

    for (i=1;i<=n*3+1;i++){
        printf "+" stars(max[i]+2)
    }
    print "+"

    printf "| %-*s ", max[1], " "

    for (i=0;i<n;i++){
        printf "| %-*s ", max[2+i*3],"Wins"
        printf "| %-*s ", max[3+i*3],"Losses"
        printf "| %-*s ", max[4+i*3],"Ratio"
    }
    print("|")

    for (i=1;i<=n*3+1;i++){
        printf "+" stars(max[i]+2)
    }
    print "+"

    for (r = 1; r <= rows; r++) {
        printf "| %-*s ", max[1], table_data[r,1]

        for (c = 2; c <= cols; c++) {
            printf "| %-*s ", max[c], table_data[r,c]
        }
        print "|"
    }
    for (i=1;i<=n*3+1;i++){
        printf "+" stars(max[i]+2)
    }
    print "+"
}'


  
