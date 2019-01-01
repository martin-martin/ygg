# YGG - revisit crusty files

Re-surface random files for bite-sized revisiting!

Take a look, remember, smile, think, work on it, delete it, ... - just do whatever seems appropriate!

Clean that gunk! :)

Happy new year everyone!

## How To

### Setup (one-time)

1) Clone this repo, make and activate a virtual environment and `pip install -r requirements.txt`
2) Run `python create_db.py` to create the SQLite database file
3) Edit the `DOC_DIR` variable in `fetch_files.py` to the folder you want to index
4) (Optional) edit which _file types_ you want to index by adding/removing extensions to the `f_types` list
in `fetch_files.py`
5) Run `python fetch_files.py` to scan your chosen directory and populate the SQLite db

### Revisit (daily?)

Whenever you want to pick and revisit a random file, you can now run `python revisit.py` and it'll open it up for you.

**Create a CRON job** if you want this to happen on a regular and automated basis.


---


## Being realistic

Setting up this revisit db for my `Documents` folder with the current settings
gives a sobering outlook:

```
>>> len(all_files)
115972
>>> x = len(all_files) / 365
>>> x
317.73150684931505
```

If I revisit one file each day, that process will take me nearly 318 years.

And that's **one round** (without adding new files) - and only the files I have on
this disk. There's more. lol.

So I'd strongly recommend to improve on the revisit method.

### Some suggestions
 
- **Limit file types** - maybe you're writing `.rtf` only, and just want to see your writings
- **Select folders** - have a dump folder you want to clean? Maybe `Downloads`? Set that one as the base `DOC_DIR`
when creating your db 
- **Many-a-day** - of course that makes it quicker

## Remember

This is naive code that picks _everything_ of the specified file types sitting somewhere down the tube
of the specified folder. It's as far from A.I. as you can possibly get.

Therefore it'll yield tons of files that are not files of your personal interest (e.g. some `LICENSE.txt` from 
a random node project - but maybe you _do_ want to revisit those!).

Otherwise, what you can always do is:

![home organization - just give up](https://imgs.xkcd.com/comics/home_organization.png)
[_xkcd 1077 - Home Organization_](https://xkcd.com/1077/)

Only that we're already in the digital realm...

## Contributing

Or you can contribute to improve this project! :)

If you have ideas write to me or simply build stuff and PR. Contributors are very welcome.