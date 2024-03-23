
# Roblox External BloxBurg AutoFisher Bot 


![Example Image of Script](https://i.ibb.co/f8YpGJk/Screen-Shot-2024-03-22-at-10-57-26-AM.png
)



I got the idea for this project when I was playing this populr Roblox game where you have to take up numerous jobs and work to make money. In turn, that money is used to build your house, purchase vehicles, etc. However, there was one job that I realized was possible to bot using openCV and python which was the fishing game. 

The game mechanics were simple:


- Cast your fishing rod
- when the Bob is underwater pull rod and ear money

So the code does the following to determine if the Bob is underwater:
- If the number of gray pixels is zero after pre-processing (grayscale + Gaussian Blur + binarization) then the bob is underwater

**However, before this, the user needs to enter a template image which will have BBOX from Mac's built-in previe editing. **

![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)


**You must follow the bounding boxes in the example picture found in the SAMPLES folder, black for the cast button and RED for the bob, try to get as much of the bob as possible!**

**Remmeber this was mainly a POC script to show you how simple external python pixel bots can be even without the use of programs such as AHK or other pixel bot automations that are more Windows-oriented leaving Mac homeless!**

![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

**Before** running the script make sure to:
- 1: Have **screencapture** installed (should be on your mac by default)
- 2: Run "**python3 -m pip install -r requirements.txt**"
- 3: Create proper Bounding boxes using mac preview and same colors as found in our example **Samples** folder
- 4: Run the script with sudo: "**sudo python3 ./main.py**"

