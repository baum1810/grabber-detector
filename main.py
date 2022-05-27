from os import system
#coded by https://github.com/baum1810
words = ["token","appdata","leveldb","Local Storage","discord_webhook","applicationdata","dhooks","grab","steal",".log",".ldb", "webhook"]
paths = ["\\Discord", "\\discordcanary", "\\discordptb", "\\Google\\Chrome\\User Data\\Default", "\\Opera Software\\Opera Stable", "\\BraveSoftware\\Brave-Browser\\User Data\\Default", "\\Yandex\\YandexBrowser\\User Data\\Default", "\\Local Storage\\leveldb"]
links = ["https://myexternalip.com/raw", "https://api.ipify.org"]
files = ["Loginvault.db", "passwords.txt", "cookies.txt","\\Google\\Chrome\\User Data\\Default\\Cookies", "Local\\Google\\Chrome\\User Data\\Default\\History", "launcher_accounts.json"]
def main():
    counter = 0
    wordcounter = 0
    webhookcounter = 0
    regexcounter = 0
    pastebincounter = 0
    linkcounter = 0
    pathcounter = 0
    filecounter = 0
    regexlines = ""
    wordlines = ""
    linklines = ""
    pathlines = ""
    filelines = ""
    system("cls")
    print("coded by https://github.com/baum1810\nThis tool isnt for advanced grabbers and just checks for common grabber code it wont detect encrypted code so this tool isnt going to protect to 100% against grabbers but it can help against Skidz so much fun with this tool\n")
    file = input("Drag the file you want to scann and press enter\n> ")
    if ".py" in file:
        with open(file) as f:
            for line in f:
                counter +=1
                if "https://pastebin.com" in line:
                    pastebincounter +=1
                    test = line.split('https://pastebin.com/raw/')
                    if '"' in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = test.replace(",", "")
                        test = str(test).split('"')

                        print(f'pastebin found https://pastebin.com/raw/{test[0]} Line {counter}')
                    elif "," in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = str(test).split(",")
                        print(f'pastebin found https://pastebin.com/raw/{test[0]} Line {counter}')
                    elif ")" in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = str(test).split(")")
                        print(f'pastebin found https://pastebin.com/raw/{test[0]} Line {counter}')

                if "https://discord.com/api/webhooks/" in line:
                    webhookcounter +=1
                    test = line.split("https://discord.com/api/webhooks/")

                    if "'" in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = test.replace(",", "")


                        print(f'Webhook found https://discord.com/api/webhooks/{test} Line {counter}')
                    elif '"' in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = test.replace(",", "")
                        test = str(test).split('"')

                        print(f'Webhook found https://discord.com/api/webhooks/{test[0]} Line {counter}')
                    elif "," in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = str(test).split(",")
                        print(f'Webhook found https://discord.com/api/webhooks/{test[0]} Line {counter}')
                    elif ")" in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = str(test).split(")")
                        print(f'Webhook found https://discord.com/api/webhooks/{test[0]} Line {counter}')
                elif"https://canary.discord.com/api/webhooks" in line:
                    webhookcounter+=1
                    test = line.split("https://canary.discord.com/api/webhooks")

                    if "'" in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = test.replace(",", "")


                        print(f'Webhook found https://canary.discord.com/api/webhooks{test} Line {counter}')
                    elif '"' in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = test.replace(",", "")
                        test = str(test).split('"')

                        print(f'Webhook found https://canary.discord.com/api/webhooks{test[0]} Line {counter}')
                    elif "," in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = str(test).split(",")
                        print(f'Webhook found https://canary.discord.com/api/webhooks{test[0]} Line {counter}')
                    elif ")" in test[1]:
                        test = str(test[1])
                        test = test.replace("[", "")
                        test = test.replace("]", "")
                        test = test.replace("'", "")
                        test = str(test).split(")")
                        print(f'Webhook found https://canary.discord.com/api/webhooks{test[0]} Line {counter}')


                if "[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}" in line:
                    regexcounter+=1
                    regexlines +=line
                    #print(f"suspicious Regex found Line {counter}")

                for word in words:
                    if word in line:
                        wordcounter+=1
                        wordlines+=str(counter)+ ','
                        print(word)
                        #print(f"suspicious word {word} found Line {counter}")
                for link in links:
                    if link in line:
                        linkcounter+=1
                        linklines+=str(counter)+ ','
                        #print(f"suspicious link {link} found Line {counter}")
                for path in paths:
                    if path in line:
                        pathcounter+=1
                        pathlines+=str(counter)+ ','
                        #print(f"suspicious path {path} found Line {counter}")

                for file in files:
                    if file in line:
                        filecounter+=1
                        filelines+=str(counter)+ ','
                        #print(f"suspicious file {file} found Line {counter}")


            total = wordcounter+linkcounter+regexcounter+webhookcounter+pastebincounter+pathcounter+filecounter
            if total < 2:
                risk = "Low"
            elif total <5:
                risk = "Medium"
            elif total >5:
                risk = "High"
            input(f"\nfilenames lines:{filelines}\npaths lines:{pathlines}\nlinks lines:{linklines}\nWords lines:{wordlines}\ndetected words:{wordcounter}\ndetected links:{linkcounter}\ndetected regex:{regexcounter}\ndetected webhooks:{webhookcounter}\ndetected pastebins:{pastebincounter}\ndetected paths:{pathcounter}\ndetected files:{filecounter}\nTotal Flags:{total}\nRisk:{risk}\npress enter to scann again")
            main()
main()
