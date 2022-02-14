import os;
import sys;
import subprocess;
import webbrowser;
import selenium.webdriver as webdriver;
from bs4 import BeautifulSoup;
import urllib.request;
from selenium.webdriver.chrome.options import Options

AIName='Navi';
Usernames=['Mason'];
AIinputconditions=["When I say ", "when i say ", "if i say ", "If I say ", "when I say ", "if i ask"];
inputindex="";
AIspeakconditions=["tell me", " you say "];
speakindex="";
AIrunfunc_cond=["run function", "execute function"];
runfunc_index="";
Whileloop=True;
google_search_conditions=['search google for', 'show me a search for','show me info on', 'show me information on'];
gsearchindex='';
google_searchhidden_conditions=['run a search for', 'read me info on', 'find info on', 'search info on', 'find me information on', 'find me info on', 'search for', 'what is', 'why are', 'when was', 'what are', 'who was', 'who were'];
gsearchhiddencon='';

listofyesterms=[];
listofcancelterms=[];
listofnoterms=[];

#Location placeholders
Country='';
Region='';
City='';


edgedriver="C:\Drivers\selenium_drivers\MicrosoftWebDriver.exe";
chromedriver="C:\Drivers\selenium_drivers\chromedriver.exe";

############################################################################################
#code generation functions

def AIspeak(input1, output1):
    with open("C:/Users/Mason/Documents/Project_1/Project/Main.py",'a+') as A:
        A.write('\n    if userinput==\"'+input1+'\":print(\"'+output1+'\");');
        A.flush();
        os.fsync(A.fileno());
        p1=subprocess.Popen([sys.executable,__file__]);
        p1.wait();
        

def assigninput_tofunction(inputa1, inputa2):
        with open ('C:/Users/Mason/Documents/Project_1/Project/Main.py','a+') as A:
                A.seek(0);
                newstr="def "+inputa2;
                newstr2=A.read();
                #print(newstr);
                #print (newstr2);
                if newstr in newstr2:
                        A.seek(2);
                        A.write('\n    if userinput==\"'+inputa1+'\":'+inputa2+'();');
                        A.flush();
                        os.fsync(A.fileno());
                        p1=subprocess.Popen([sys.executable,__file__]);
                        p1.wait();

#############################################################################################
#pre-programmed functions
def getlocation():

        urlI="https://mylocation.org/";
        browser=webdriver.PhantomJS('C:\Drivers\selenium_drivers\phantomjs.exe');
        browser.get(urlI);
        #links= browser.find_element_by_xpath('//*[@id="ui-accordion-accordion-panel-0"]/div/div[1]/table/tbody/tr[4]/td[2]'); 
        html=urllib.request.urlopen(urlI).read();
        site = BeautifulSoup(html, 'html.parser');
        rawinfo = site.find_all('td');
        placeholder='';
        for info in rawinfo:
                contents=info.get_text();

                if placeholder=='Country':
                        Country=contents;
                if placeholder=='Region':
                        Region=contents;
                if placeholder=='City':
                        City=contents;

                placeholder=contents;
                placeholder.strip();
        print(Region);
      

#####################################SWITCH EVERYTHING TO CHROME DRIVER###############################################

#possibly create list of specific commands to not run any other commands

#def Chromelogin();

#def function for storing memory of recent searches and clicked links etc.

#def getweather():
        
#def addtolist(List, Addedinfo):

#def getTimeandDate():

def openyoutube():
        openinchrome=input('would you like to open in Google Chrome?');
        #Have to put in chrome login function
        searchterms=input('What would you like to search?\n');

        if openinchrome == "yes" or openinchrome=='ya sure' or openinchrome=='sure why not' or openinchrome == 'ya' or openinchrome == 'sure':
                browser=webdriver.Edge(chromedriver);
        else :
                browser=webdriver.Edge(edgedriver);

        if searchterms == 'no search' or searchterms == 'nothing' or searchterms=='just browsing':
                url="https://www.youtube.com/";
                browser.get(url);
        else :
                url="https://www.youtube.com/";
                browser.get(url);
                search_box= browser.find_element_by_name("search_query");
                search_box.send_keys(searchterms);
                search_box.submit();
        
#def openyoutubewcond():        

def calculator():
        calcinput=input("input equation \n");

def integralcalculator():
        webbrowser.open('https://www.integral-calculator.com/',0 ,True);

def derivativecalculator():
        webbrowser.open('https://www.derivative-calculator.net/', 0,True);

def websearch():
        searchterms=input('What would you like to search?\n');
        url="https://www.google.com/";
        browser=webdriver.Edge(edgedriver);
        browser.get(url);
        search_box= browser.find_element_by_name("q");
        search_box.send_keys(searchterms);
        search_box.submit();

def websearchwcond(searchtermsA):
        url="https://www.google.com/";
        browser=webdriver.Edge(edgedriver);
        browser.get(url);
        search_box= browser.find_element_by_name("q");
        search_box.send_keys(searchtermsA);
        search_box.submit();
        
def websearchhidden():
        searchterms=input('What would you like to search?\n');
        if searchterms == 'cancel' or searchterms == 'actually, cancel':
                return;
        url="https://www.google.com/";
        browser=webdriver.PhantomJS('C:\Drivers\selenium_drivers\phantomjs.exe');
        browser.get(url);
        search_box= browser.find_element_by_name("q");
        search_box.send_keys(searchterms);
        search_box.submit();      
        links= browser.find_elements_by_xpath("//h3//a"); 
        
        for link in links:
                href=link.get_attribute("href");
                hrefcut=href.replace('https://www.google.com/url?q=','');
                printableurl=hrefcut.split("://")[1].split("/")[0];
                print("I found some information on  "+printableurl+". Would you like me to read it?");
                #above line has to be cleaned of messy urls

                yesorno=input("");
                yesorno=yesorno.strip();

                if yesorno =='cancel' or yesorno == 'actually nevermind' or yesorno == 'actually cancel' or yesorno == 'nevermind':
                        break;

                if yesorno == "yes" or yesorno=='ya sure' or yesorno=='sure why not' or yesorno == 'ya' or yesorno == 'sure':
                        html=urllib.request.urlopen(href).read();
                        site = BeautifulSoup(html, 'html.parser');
                        contents = site.find_all('p');
                        for x in contents:
                                paragraph=x.get_text();
                                print(paragraph);
                        break;
        
#####Selenium is sometimes returns incorrect url
#####Maybe consider adding headings to web printed information

def websearchhiddenwcond(SearchtermsHidden):
        url="https://www.google.com/";
        browser=webdriver.PhantomJS('C:\Drivers\selenium_drivers\phantomjs.exe');
        browser.get(url);
        search_box= browser.find_element_by_name("q");
        search_box.send_keys(SearchtermsHidden);
        search_box.submit();      
        links= browser.find_elements_by_xpath("//h3//a"); 
        
        for link in links:
                href=link.get_attribute("href");
                hrefcut=href.replace('https://www.google.com/url?q=','');
                printableurl=hrefcut.split("://")[1].split("/")[0];
                print("I found some information on  "+printableurl+". Would you like me to read it?");
                

                yesorno=input("");
                yesorno=yesorno.strip();

                if yesorno =='cancel' or yesorno == 'actually nevermind' or yesorno == 'actually cancel' or yesorno == 'nevermind':
                        break;

                if yesorno == "yes" or yesorno=='ya sure' or yesorno=='sure why not' or yesorno == 'ya' or yesorno == 'sure':
                        html=urllib.request.urlopen(href).read();
                        site = BeautifulSoup(html, 'html.parser');
                        contents = site.find_all('p');
                        for x in contents:
                                paragraph=x.get_text();
                                print(paragraph);
                        break;

#def searchwolframalpha(QueryTerms):

############################################################################################
#code for generating new code if input calls for it or running searches with given conditions

while(1):

    userinput=input("");
    userinput = userinput.strip();

    if userinput=="run a search for me":websearchhidden();continue;

    if any(c in userinput for c in AIinputconditions) :
        for x in AIinputconditions:
                if x in userinput:
                        inputindex=x;
                        #print(inputindex);
        
    if any(c in userinput for c in AIspeakconditions) :
                for y in AIspeakconditions:
                        if y in userinput:
                                speakindex=y;
                                #print(speakindex);
                phrase1=userinput.split(inputindex)[1].split(speakindex)[0];
                phrase2=userinput.split(speakindex,1)[1];
                phrase1=phrase1.strip();
                phrase2=phrase2.strip();
                AIspeak(input1=phrase1,output1=phrase2);       

    if any(c in userinput for c in AIrunfunc_cond) :
                for z in AIrunfunc_cond:
                        if z in userinput:
                                runfunc_index=z;
                func_phrase=userinput.split(inputindex)[1].split(runfunc_index)[0];
                func_run=userinput.split(runfunc_index,1)[1];
                func_phrase=func_phrase.strip();
                #print(func_phrase);
                func_run=func_run.replace(" ", "");
                #print(func_run);
                assigninput_tofunction(inputa1=func_phrase, inputa2=func_run);


        #if any(c in userinput for c in AIspeakconditions) :
                for y in AIspeakconditions:
                        if y in userinput:
                                speakindex=y;
                                #print(speakindex);
                phrase1=userinput.split(inputindex)[1].split(speakindex)[0];
                phrase2=userinput.split(speakindex,1)[1];
                phrase1=phrase1.strip();
                phrase2=phrase2.strip();
                AIspeak(input1=phrase1,output1=phrase2);       

    if any(c in userinput for c in google_search_conditions):
            for x in google_search_conditions:
                    if x in userinput:
                            gsearchindex=x;
            Sterms=userinput.split(gsearchindex,1)[1]; 
            Sterms.strip();
            websearchwcond(searchtermsA=Sterms);       

    if any(c in userinput for c in google_searchhidden_conditions):
            for x in google_searchhidden_conditions:
                    if x in userinput:
                            gsearchhiddencon=x;
            Sterms=userinput.split(gsearchhiddencon,1)[1]; 
            Sterms.strip();
            websearchhiddenwcond(SearchtermsHidden=Sterms);     

    #here on is all self generated code

    if userinput=="hi":print("hello");
    if userinput=="i need a calculator":calculator();
    if userinput=="calculate":calculator();
    if userinput=="open integral calculator":integralcalculator();
    if userinput=="open derivative calculator":derivativecalculator();
    if userinput=="i need to calculate a derivative":derivativecalculator();
    if userinput=="open google":websearch();
    if userinput=="i need you to search something for me":websearchhidden();
    if userinput=="search something for me":websearchhidden();
    if userinput=="i need to google something":websearch();
    if userinput=="i need to calculate an integral":integralcalculator();
    if userinput=="did it work":print("I think it did");
    if userinput=="hello":print("hi how are you");
    if userinput=="Hello":print("Hi, how are you?");
    if userinput=="im great thanks":print("I'm glad to hear that");
    if userinput=="hey navi":print("hello!");
    if userinput=="open youtube":openyoutube();
    if userinput=="test":getlocation();
    if userinput=="hey navi you up":print("Of course!");