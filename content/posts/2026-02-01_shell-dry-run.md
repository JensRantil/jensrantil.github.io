+++
date = 2026-02-01T22:05:35+02:00
title = "A shell dry run trick"
description = "Review all shell commands before executing them. Avoid a catastrophe. Profit."
tags = ["Shell"]
slug = "a-shell-dry-run-trick"
+++
I recently read the blog post ["In Praise of –dry-run"][dry-run-praise]. I love dry-run modes! They are immensely useful. The blog post reminded me of a small terminal trick that I have used for years, but never shared with the Internet:

[dry-run-praise]: https://henrikwarne.com/2026/01/31/in-praise-of-dry-run/

## An example

Imagine you want to download many profile pictures from the Internet. All the images are stored in a <abbr title="Comma-separated values">CSV</abbr> file containing 1) the name of the person and 2) a URL to the image. Something like this:
```csv
name,url
peter,https://images.example-cdn.io/gallery/pt.png
lisa,https://cdn.fictionalassets.net/ui/icons/liz.png
maria,https://media.mocksite.org/uploads/2026/01/mariaa.png
caren,https://assets.imaginarylab.com/products/c.png
chris,https://static.placeholderhub.dev/images/christoffer_columbus.png
```
You would like to download every image and store it locally on your disk as `{name}.png`. Ie. the urls `https://images.example-cdn.io/gallery/pt.png` would be downloaded to `peter.png`.

The way I would approach this would be as a 3-step process:

1. Generating the shell commands that would do all the work. (dry-run)
2. Reviewing the commands.
3. Executing all the commands.

Let me go through these steps one after the other:

## Generating the shell commands (dry-run)

Initially, I would figure out how to download _one_ image and verify that the command succeeded:
```sh
$ curl -o peter.png 'https://images.example-cdn.io/gallery/pt.png'
$ ls
peter.png
$
```
I would probably also want `curl` to fail on error, output errors, and exit non-zero on error:
```sh
$ rm peter.png
$ curl --fail --show-error --silent -o peter.png 'https://images.example-cdn.io/gallery/pt.png'
$ ls
peter.png
$
```
My next step would be to generate the shell command for that same image. First step would be to skip the first line of the CSV file:
```sh
$ cat images.csv | tail -n +2
peter,https://images.example-cdn.io/gallery/pt.png
lisa,https://cdn.fictionalassets.net/ui/icons/liz.png
maria,https://media.mocksite.org/uploads/2026/01/mariaa.png
caren,https://assets.imaginarylab.com/products/c.png
chris,https://static.placeholderhub.dev/images/christoffer_columbus.png
```
Since I would only want to recreate my `curl` execution, I would focus on the first line:
```sh
$ cat images.csv | tail -n +2 | head -n 1
peter,https://images.example-cdn.io/gallery/pt.png
```
From here on I would generate the `curl` command using my tool of choice, `awk`:
```sh
$ cat images.csv | tail -n +2 | head -n 1 \
  | awk -F, '{print "curl --fail --show-error --silent -o", $1 ".png", $2;}'
curl --fail --show-error --silent -o peter.png https://images.example-cdn.io/gallery/pt.png
```
Notice how this would _not_ execute anything. It would simply output what the shell command would look like. Dry-run, FTW! To reduce the likelihood of any weird escape sequences[^1], I would probably also wrap the URL in single quotes:
```sh
$ cat images.csv | tail -n +2 | head -n 1 \
  | awk -F, '{print "curl --fail --show-error --silent -o", $1 ".png", "'\''" $2 "'\''" ;}'
curl --fail --show-error --silent -o peter.png 'https://images.example-cdn.io/gallery/pt.png'
```

[^1]: I am well aware of other escape attack vectors here, but let's assume the file came from a trusted source!

Removing `head -n 1`, I would now have all the commands needed to download the images:
```sh
$ cat images.csv | tail -n +2 \
  | awk -F, '{print "curl --fail --show-error --silent -o", $1 ".png", "'\''" $2 "'\''" ;}'
curl --fail --show-error --silent -o peter.png 'https://images.example-cdn.io/gallery/pt.png'
curl --fail --show-error --silent -o lisa.png 'https://cdn.fictionalassets.net/ui/icons/liz.png'
curl --fail --show-error --silent -o maria.png 'https://media.mocksite.org/uploads/2026/01/mariaa.png'
curl --fail --show-error --silent -o caren.png 'https://assets.imaginarylab.com/products/c.png'
curl --fail --show-error --silent -o chris.png 'https://static.placeholderhub.dev/images/christoffer_columbus.png'
```

## Reviewing and testing a command

Once I had all the shell commands generated, I would skim through them to see if anything looked odd. I would also pick one command at random, copy/paste it into my terminal, and execute it to see that it works:
```sh
$ curl --fail --show-error --silent -o maria.png 'https://media.mocksite.org/uploads/2026/01/mariaa.png'
$ ls
maria.png
peter.png
$
```

## Executing all the commands

If all looks good, I would **pipe all the output into a shell (`sh`, `bash`, ...) to execute**:
```sh
$ cat images.csv | tail -n +2 \
  | awk -F, '{print "curl --fail --show-error --silent -o", $1 ".png", "'\''" $2 "'\''" ;}' \
  | sh
$ ls
caren.png
chris.png
lisa.png
maria.png
peter.png
$
```

## Bonus: Slow commands
If the execution was really slow, I would use `pv` instead of `cat` to get an ETA and the number of images downloaded per second:
```sh
$ pv --line-mode images.csv | tail -n +2 \
  | awk -F, '{print "curl --fail --show-error --silent -o", $1 ".png", "'\''" $2 "'\''" ;}' \
  | sh
4,00  0:00:05 [10   /s] [=====================================>                    ]  66% ETA 0:15:00
$
```
If I needed to parallelise downloads, I would use `xargs`:
```sh
$ pv --line-mode images.csv | tail -n +2 \
  | awk -F, '{print "curl --fail --show-error --silent -o", $1 ".png", "'\''" $2 "'\''" ;}' \
  | xargs -P10 -I{} sh -c '{}'
4,00  0:00:05 [10   /s] [=====================================>                    ]  66% ETA 0:15:00
$
```
to download 10 files in parallel.

## Closing thoughts

Generating shell commands, verifying them, and then piping them into a shell can be a powerful way to quickly get repetitive tasks done in a safe manner.