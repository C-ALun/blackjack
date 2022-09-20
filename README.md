<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">PROJECT_BLOG</h3>

  <p align="center">
    It's an awesome readme to jumpstart my projects and record my growth progress!
    <br />
    <a href="https://github.com/C-ALun/blackjack/blob/main/my_project.py">View My_demo</a>
    ·
    <a href="https://github.com/C-ALun/blackjack/blob/main/prof_project.py">View Prof_demo</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

I'm joining a 100 Days of Coding program <a href="https://github.com/C-ALun/blackjack/blob/main/my_project.py">on Udemy</a>. 

Here's why:
* Get used to using Python language 
* Improve coding skills and style by through projects provided
* Record and motivate myself by pushing on GitHub

I would point out my code and prof code to compare them and highlight how I can become better.

## Session of dealing Card
```
MY_PROJECT:

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
	return random.choice(cards)

#deal user a starting hand of 2 random card values
for _ in range(2):
  chosen_card = deal_card()
  player_card_list.append(chosen_card)
  player_score += chosen_card
  
#deal computer a starting hand of 2 random card values
for _ in range(2):
  chosen_card = deal_card()
  computer_card_list.append(chosen_card)
  computer_score += chosen_card
```
```
 PROF_PROJECT:
 
 def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
 
 for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
```
### Problems
>Problems: **Duplicated** AND deal_card() function not **reusable**.

## Session of calculating score
```
MY_PROJECT

player_turn = True
computer_turn = True
if computer_score == 21 and player_score == 21:
  player_turn = False
  computer_turn = False
elif computer_score == 21 or player_score == 21:
  if computer_score == 21:
    computer_turn = False
  else:
    player_turn == False

if player_score > 21:
  player_card_list.remove(11)
  player_card_list[0] = 1
  player_score -= 10
elif computer_score > 21:
  computer_card_list.remove(11)
  computer_card_list[0] = 1
  computer_score -= 10

if player_score > 21:
  if 11 in player_card_list:
    player_card_list[player_card_list.index(11)] = 1
    player_score -= 10
    
    .
    .
    .
```
```
PROF_PROJECT

def calculate_score(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
```
### Problems
>Problems: **Complex** AND Some codes are similar, could be written in a function and make it reusable and more maintainable.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!--
### Built With
This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

*** [![Next][Next.js]][Next-url]
*** [![React][React.js]][React-url]
*** [![Vue][Vue.js]][Vue-url]
*** [![Angular][Angular.io]][Angular-url]
*** [![Svelte][Svelte.dev]][Svelte-url]
*** [![Laravel][Laravel.com]][Laravel-url]
*** [![Bootstrap][Bootstrap.com]][Bootstrap-url]
*** [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>
!-->


<!-- GETTING STARTED -->
<!--
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>
!-->


<!-- USAGE EXAMPLES -->
<!--
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

!-->

<!-- ROADMAP -->
## Roadmap

- [ ] Deal both user and computer a starting hand of 2 random card values.
- [ ] Detect when computer or user has a blackjack. (Ace + 10 value card).
- [ ] If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).
- [ ] Calculate the user's and computer's scores based on their card values.
- [ ] If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
- [ ] Reveal computer's first card to the user.
- [ ] Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
- [ ] Ask the user if they want to get another card.
- [ ] Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
- [ ] Compare user and computer scores and see if it's a win, loss, or draw.
- [ ] Print out the player's and computer's final hand and their scores at the end of the game.
- [ ] After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
- [ ] See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
<!--
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- ACKNOWLEDGMENTS -->
<!--
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
