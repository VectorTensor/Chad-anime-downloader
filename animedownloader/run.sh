animename=Tokyo_Revengers
n=000
start=000
end=002
counter=$start

if [ -d $animename ]
then
    cd $animename
else
    mkdir $animename
    cd $animename
fi

c="000"
converter () {
    case $counter in
        0)
            c="000"
            ;;
        1)
            c="001"
            ;;

        2)
            c="002"
            ;;
        3)
            c="003"
            ;;
        4)
            c="004"
            ;;
        5)
            c="005"
            ;;
        *)
            echo error out of bound
            ;;
    esac

    
}
while [ $counter -le $end ]
do
    converter
    url="https://21.manga47.net/${animename}/${animename}_${c}.mp4"

    filename=${animename}_${counter+1}
   # curl $url --output "${filename}.mp4" 
   cp "${filename}.mp4" $animename

   echo $url
   echo $filename
   ((counter ++))
    
done


