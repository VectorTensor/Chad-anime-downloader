animename=Tokyo_Revengers
n=000
start=000
end=002
counter=$start
while [ $counter -le $end ]
do
    url="https://21.manga47.net/${animename}/${animename}_${counter}.mp4"

    filename=${animename}_${counter+1}
    curl $url --output "${filename}.mp4" 
done


