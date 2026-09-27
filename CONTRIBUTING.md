# Contribution Guidelines

[English](CONTRIBUTING.md) | [简体中文](CONTRIBUTING.zh-CN.md)

Thank you for helping make Awesome Chess better! ♟️ Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## What belongs on the list

Awesome Chess is a **curated** list, not a directory of everything chess-related. A resource should be:

- **Genuinely useful** to players, coaches, developers or researchers, and ideally something you have used yourself.
- **Alive** — the website works, or the project was updated in the last couple of years. Exceptions are made for resources of lasting historical or educational value (classic engines, papers, public-domain books).
- **Free or high quality.** Paid products are welcome when they are widely recognized as best in class; say so in the description when something is paid.
- **Not self-promotion spam.** Adding your own project is fine if it meets the bar above and you disclose it in the pull request.

## Adding a resource

1. Search the list (and the open pull requests) to make sure the resource is not already there.
2. Add it to the most relevant section of **both** [`README.md`](README.md) and [`README.zh-CN.md`](README.zh-CN.md). If you can't write Chinese, add the English description to both files and a maintainer will translate it.
3. Use this format:

   ```md
   - [Name](https://link) - Short description ending with a period.
   ```

   - Use the resource's official name and its canonical link (the official website, or the GitHub repository).
   - Keep descriptions short and objective: say what it *is*, not that it is "awesome" or "the best".
   - Start the description with a capital letter and end it with a period (Chinese: a full-width `。`).
   - Avoid marketing words, emojis and exclamation marks.
   - New entries go **at the bottom** of their section unless the section has an obvious order.
4. Run the checks locally:

   ```sh
   npx awesome-lint README.md
   python3 scripts/check_readme_sync.py
   ```

5. Open a pull request with a descriptive title such as `Add Stockfish` and fill in the template. One resource (or one tightly related change) per pull request, please.

## Updating or removing a resource

- **Broken or outdated link?** Open a pull request with the fix, or [open an issue](https://github.com/SudoAI-DEV/awesome-chess/issues/new/choose).
- **Something should be removed?** Open an issue or pull request explaining why (dead, abandoned, superseded, low quality).
- Suggestions for new sections or restructuring are welcome — open an issue first so we can discuss.

## Automated checks

Every pull request runs:

- [`awesome-lint`](https://github.com/sindresorhus/awesome-lint) on the English README.
- A sync check that makes sure the English and Chinese READMEs list the same links.
- [`lychee`](https://github.com/lycheeverse/lychee) to catch dead links. The link checker also runs weekly and opens an issue when something breaks.

Thank you for your contribution!
