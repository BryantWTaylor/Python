print() #blank line
# instructions to the user
print('You are about to embark on an adventure!')
print('To choose what you want to do please type in one of the options that is in ALL CAPS.\n')

# begining of the story code
first_choice = input('You are walking down a beautiful wooded path. The path splits in front of you.\nYou can go RIGHT, LEFT, or STRAIGHT. What path do you choose? ')

if first_choice.lower() == 'right':
    second_choice_a = input('\nThe path gets darker and darker and you find yourself stumbling through a thick brush.\nBy pure coincidence you see a MACHETE and an AXE. Which do you pick up? ')
    if second_choice_a.lower() == 'machete':
        third_choice_a = input('\nYou picked up a great tool for cutting through the brush. You make it through the thickness of the brush and find a sleeping bear.\nYour stomach rumbles as you decide if you should ATTACK to try and get some fresh meat, or CONTINUE on your way. Which do you choose? ')
        if third_choice_a.lower() == 'attack':
            print('\nYou attack the sleeping bear with your machete and get in a good blow. But the bear wakes up in a grumpy rage. \nYou get in a fight for your life and take some devastating hits, but you miraculously survive.\nNow hopefully you will find a way to start a fire... ')
        elif third_choice_a.lower() == 'continue':
            print("\nYou decide to let sleeping bears lie and you continue on your way.\nBut what luck! You happen across a large bush of wild berries and are able to eat to your heart's (or stomach's) content.")
        else:
            print("\nUnfortunately that was not an option.\nBecause you couldn't make a decision you just froze there looking at the bear. Hopefully he doesn't wake up and decide he is hungry.\nThe end.")

    elif second_choice_a.lower() == 'axe':
        third_choice_b = input('\nThe axe is a great tool for cutting down trees, but maybe not too great at getting you through the brush.\nYou start to noisily cut through the brush when you hear something big coming toward you.\nYou look and notice a big bear that you most likely woke up with all the noise you were making. Do you RUN or do you stand and FIGHT? ')
        if third_choice_b.lower() == 'run':
            print('\nThat is probably a good call, that bear looked enormous!\nUnfortunately, as you are struggling to run back through the brush you fall into a hole.\nYou hear the bear pass you by, but now you have to figure out how you are going to get out of the hole...')
        elif third_choice_b.lower() == 'fight':
            print("\nYou figure with the thick brush you might stand a chance. You fight your hardest.\nYou dodge, crawl, and get in some good swings at the bear, but he is wearing you down.\nThe bear is coming to finish you off when you desperately throw your axe toward it.\nBy some miracle the axe slices into the neck of the bear and he goes down.\nYou realize your luck won't last and you need to get out of these woods... while you still can.")
        else:
            print('\nThat was definitely not an option.\nThe bear charged right toward you. You are totally bear chow.\nThe end.')

    elif second_choice_a.lower() == 'both':
        third_choice_c = input('\nWell, well, well! Look who thinks they can do it all! Well it turns out you can!\nThis machete and axe are actually a paired set that have been enchanted by Wizard Gnomes!\nYou can feel the power coursing through you as you easily slice your way through the brush. You make it to a clearing and find a small cottage.\nDo you go INSIDE to try and get some rest or do you press FORWARD and trust in your newfound magical items? ')
        if third_choice_c.lower() == 'inside':
            fourth_choice_a = input('\nYou go inside of the lovely cottage only to find a gnome!\nThis little gnome named Jeremy is mad that you have his enchanted artifacts and with a snap of his fingers you feel them yank out of your grasp.\n“Jeremy, NOOOO!” you yell as you feel more than your weapons leaving your body...\nYou wake up dazed and confused. You are not even sure what your name is.\nYou sit alone in a cottage and while looking around you see a heavy DOOR off to the side and a TRAP door in the floor.\nWhich do you go through? ')
            if fourth_choice_a.lower() == 'door':
                print('\nYou go through the heavy door and see a gnome that looks vaguely familiar.\nHe says to you "Well it looks like you woke up, now it is time to put you to work."\nClearly he knows you, but you are unsure about this whole situation. How did you even get here?')
            elif fourth_choice_a.lower() == 'trap':
                print('\nYou crawl over the trap door and struggle to get it lifted but with all of your remaining strength you mangage it.\nYou are in a dark and musty tunnel and perhaps this will lead you to escape. But escape from what?\nYou just feel like there is something that you are missing.\nHopefully the pieces will settle into place as your journey continues.')
            else:
                print('\nNot making a correct choice can lead to disaster and it totally did.\nYou just layed in the cottage and gnomes eventually came and fed you to their savage gophers.\nThe end.')
        elif third_choice_c.lower() == 'forward':
            print("\nYou have the utmost confidence in your newfound enchanted items.\nYou don't need to stop and rest! You can do anything that you put your mind to!")
        else:
            print("\nAs you don't make a valid choice and just stand outside of the cottage, you hear the start of madness creep into your mind.\nAre your enchanted items driving you crazy, or is it just idleness..?" )
    else:
        print("\nThat wasn't one of the options. Unfortunately you just turned in circles until you passed out. The end.")

elif first_choice.lower() == 'left':
    second_choice_b = input('\nYou find the trees are growing more sparse and the ground is becoming almost sandy. You might be heading into a desert.\nDo you go BACK and try to find some water or do you PUSH forward and just see what happens? ')
    if second_choice_b.lower() == 'back':
        third_choice_d = input('\nYou turn around and retrace your steps but nothing really looks familiar. The woods are looking more ominous than they did before.\nHowever now you hear some running water nearby. Do you LEAVE the path to go and look for water or do you STAY on the path? ')
        if third_choice_d.lower() == 'leave':
            print('\nYou step off the path with a sense of foreboding, and you think “Maybe I will never see the path again.”\nBut you also know that you can not survive without water.\nSo you are willing to roll the dice and take that chance.')
        elif third_choice_d.lower() == 'stay':
            print('\nYou decide to stay on the path, because the path means direction and the possibility of escape.\nYou just hope that you escape or find water before you bite the dust.')
        else:
            print('\nThat was not a valid choice. While you did not choose correctly a giant buzzard swooped down and snatched you up. \nThe end.')
    elif second_choice_b.lower() == 'push':
        third_choice_e = input('\nYou push forward down the path as it does indeed continue to get more and more sandy.\nHowever when it does fully turn into a desert you notice that there are very tall cairns that mark the path forward.\nThe path leads you to an oasis with fresh, clear water.\nIn that oasis you find a cave, do you go inside to EXPLORE or stay OUTSIDE and enjoy your time in water and the sun? ')
        if third_choice_e.lower() == 'explore':
            print('\nYou go into the depths of the cave with only the light from the entrance to guide you.\nYou find a large open room in the cave with light filtering down from a hole in the ceiling.\nYou see a vast pile of gold and jewels. Oh how exploring has paid off!')
        elif third_choice_e.lower() == 'outside':
            print("\nYou stay outside and float in the crystal clear water. Your eyes close and you drift in and out of consciousness. \nBut your eyes snap open and you see the tip of a sword pointing at you.\nOthers have come in search of a nearby treasure and they don't want you to get in their way.")
        else:
            print("\nThat was not a valid option, and wouldn't you know it, the oasis ended up being a mirage.\nThe end.")
    else:
        print("\nThat wasn't an option. But it turns out you were standing in quicksand.\nYou were slowly pulled into the sand because you didn't make a decision.")

elif first_choice.lower() == 'straight':
    second_choice_c = input("\nYou don't let the other options distract you as you push forward. You notice that your path starts to get steeper and steeper.\nSoon you are heading up the side of a mountain.\nThe path starts to use SWITCHBACKS but you find a CLIMBING pick that you could use to cut through them. Which do you choose? ")
    if second_choice_c.lower() == 'switchbacks':
        third_choice_f = input('\nSwitchbacks will save you energy and perhaps even time, so you make your way up the serpentine switchbacks.\nYou finally crest the ridge of the mountain and see a dazzling view of the valley below.\nDo you stay and enjoy the VIEW or do you start making your way DOWN the other side of the mountain? ')
        if third_choice_f.lower() == 'view':
            print("\nYou decided to stay and enjoy the wonderful view.\nIt is often worthwhile to take some time to relax and enjoy your surroundings. This time it paid off as well.\nThe wizard of the mountain joins you on the ridge and gives you a medallion.\nHe doesn't say what it does, only time will tell.")
        elif third_choice_f.lower() == 'down':
            print('\nYou decide not to waste any time and you head down the mountain.\nYou make it down with relative ease and you notice that you are recognizing the surroundings.\nOddly enough it seems as if you are walking down a beautiful wooded path. The path splits in front of you...')
        else:
            print('\nThat was not a valid answer. You stood there waiting and you were struck by a meteor.\nThe end.')
    elif second_choice_c.lower() == 'climbing':
        third_choice_g = input('\nYou decide to use the tools you have at your disposal.\nAs you cut between the switchbacks you eventually come across an abandoned mine shaft.\nDo you DESCEND or do you PURSUE your current course cutting through the switchbacks? ')
        if third_choice_g.lower() == 'descend':
            print("\nYou descend into the dark depths of the abandoned mine shaft.\nOddly you don't see the spray paint and empty cans that you expected, but you feel like something is watching you.\nYou quicken your pace as your startled mind tells you it is your best chance at getting away.\nHopefully there are multiple entrances to this mine and therefore, multiple exits...")
        elif third_choice_g.lower() == 'pursue':
            print('\nYou remember that Danger is not your middle name and you keep pushing forward up the mountain.\nIt is a lot of effort, but you are eventually rewarded by getting to the top and are greeted by an Elf.\nHe congratulates you on your quest and gives you an enchanted iron necklace.\nHe says that it will protect you from the mirage of the forest and help you on your path.')
        else:
            print('\nThat was not an option, you unfortunatly were overtaken by a group of thugs.\nThey took everything of value from you and left you for dead.\nThe end.')
    else:
        print('\nThat was not one of the options.\nYou stood there staring so long that you lost your footing, fell down the mountain and smacked your head on a rock.\nThe end.')
else:
    print("\nTurns out that wasn't one of the options, you waited around until you starved to death. The end.")