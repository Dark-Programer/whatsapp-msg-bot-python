<h1>Automated Message Sender</h1>

<p>This Python script allows you to automate sending messages through WhatsApp using PyAutoGUI.</p>

<h2>Requirements</h2>

  <ul>
    <li>Python 3.x</li>
    <li>PyAutoGUI library (<code>pip install pyautogui</code>)</li>
  </ul>

<h2>Usage</h2>

  <ol>
    <li>Make sure you have WhatsApp web open in your browser and positioned the cursor on the chat/contact where you want to send messages.</li>
    <li>Run the Python script.</li>
    <li>After a specified delay, the script will prompt you to enter the message you want to send and the number of times you want to send it.</li>
    <li>Once you've entered the message and the number of repetitions, the script will simulate typing and sending the message through PyAutoGUI.</li>
  </ol>

<h2>How It Works</h2>

<p>The script utilizes the PyAutoGUI library to automate keyboard and mouse interactions.</p>

  <ol>
    <li>The script starts by importing the necessary libraries, pyautogui for automating keyboard and mouse actions, and time for adding delays.</li>
    <li>After a short delay to switch to the WhatsApp window, the user is prompted to input the message they want to send and the number of times they want to send it.</li>
    <li>Inside the loop, the script writes the message using pyautogui.write() and simulates pressing the "Enter" key to send the message.</li>
    <li>A small delay of 0.5 seconds is added between each message to avoid flooding the chat.</li>
  </ol>

<h2>Disclaimer</h2>

<p>Automating interactions with websites or applications, including WhatsApp, may violate their terms of service. Use this script responsibly and ensure compliance with all relevant laws and regulations.</p>
