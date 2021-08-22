animename=Tokyo_Revengers
# name of the anime space is replaced with underscore _

start=000 #start of the episode => start_episode-1
end=2# end of the episode => end_episode-1
counter=$start
# Makes the anime directory if its not already present and goes to the directory
if [ -d $animename ]
then
    cd $animename
else
    mkdir $animename
    cd $animename
fi

c="000"
# this function converts interger code to string code to make the url correct

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
    esac

    
}
home=https://21.manga47.net
manga47 () {


while [ $counter -le $end ]
do
    converter
    url="${home}/${animename}/${animename}_${c}.mp4"

    filename=${animename}_${counter+1}
    curl $url --output "${filename}.mp4" 
   cp "${filename}.mp4" $animename

   ((counter ++))
    
done
}
manga47 


