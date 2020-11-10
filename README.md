# One Heaven - Ren'Py demo

This is a small demo I made to show Alma Ren'py. It can be run as any other project by cloning this
respository into the Ren'py projects folder. On Windows it is in user documents by default. On Linux,
you should probably make sure to set a proper project folder, but otherwise `/usr/share` is default.

# Running and building

The game can be ran by simply using the `Launch` button in Renpy GUI. This should launch a 1280x720
window with the game or give you an error in case there is a problem.

To build the game, click the `Build Distributions` button in the launcher, then make sure only the
`PC: Windows and Linux` option is selected, Macintosh x86 is deprecated as a whole architecture,
so it no longer makes any sense to build for it

# Editing the game

If you don't have an editor with proper support, get yourself [Atom](https://atom.io/) and install
the [Renpy syntax package](https://atom.io/packages/language-renpy). It also helps to set Atom as
your default editor if you want to use the Renpy GUI to open files.

- The main code of the game is in `skript.rpy`, for adding other chapters, it is not a bad idea to
  move them into their own files
- configuration is in `options.rpy`, see the wiki for more info
- GUI definitions etc are in `gui.rpy`, wiki, again
- audio files are in the `audio/` folder, it is public domain audio found on [freesound.org](https://freesound.org/)
- images are in the `images/` folder. Note that image declaration in renpy looks into this folder already,
  so you do not need to declare them with a `images/` prefix
- GUI elements are in `gui/` folder
- I threw the `ProFontExtended.ttf` font in there randomly for fun.

# Links

<https://www.renpy.org/doc/html/audio.html>
<https://www.renpy.org/doc/html/displaying_images.html>
<https://www.renpy.org/doc/html/dialogue.html>
<https://www.renpy.org/doc/html/label.html>
<https://freesound.org/>
