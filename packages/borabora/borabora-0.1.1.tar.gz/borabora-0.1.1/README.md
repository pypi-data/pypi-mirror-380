# Borabora - Command Line AI Assistant

🤖 **Borabora** is a command-line tool that converts natural language descriptions into Unix/Linux commands using Groq's lightning-fast AI models. Never forget terminal commands again!

## ✨ Features

- 🗣️ **Natural Language to Commands**: Convert plain English to Unix commands
- 🚀 **Instant Execution**: Option to execute commands immediately  
- 🔧 **Easy Configuration**: Simple API key setup
- 💡 **Smart Suggestions**: Powered by Groq's ultra-fast AI
- 🛡️ **Safe by Default**: Shows command before execution

## 📦 Installation

Install Borabora directly from PyPI:

```bash
pip install borabora
```

Or install from source:

```bash
git clone https://github.com/invisible-hand/borabora.git
cd borabora
pip install -e .
```

## 🔑 Setup

Before using Borabora, you need to configure your Groq API key:

1. Get your API key from [Groq Console](https://console.groq.com/keys)
2. Run the configuration command:

```bash
borabora --config
```

3. Enter your API key when prompted

Alternatively, you can set the environment variable:

```bash
export GROQ_API_KEY="your-api-key-here"
```

## 🚀 Usage

### Basic Usage

Convert natural language to commands:

```bash
borabora list all files in the current folder as a list
# Output: 💡 Suggested command: ls -al

borabora push code  
# Output: 💡 Suggested command: git push origin main

borabora show disk usage
# Output: 💡 Suggested command: df -h

borabora find all python files
# Output: 💡 Suggested command: find . -name "*.py"
```

### Execute Commands (Default Behavior)

Borabora will prompt you to execute commands by default:

```bash
borabora show current directory
# Output: 💡 Suggested command: pwd
# Execute this command? (y/N): y
# 🚀 Executing: pwd
# /Users/username/current/path
```

### Dry-Run Mode

Use the `--dry-run` or `-d` flag to only show commands without executing:

```bash
borabora -d show current directory
# Output: 💡 Suggested command: pwd
# 🔍 Dry-run mode: Command not executed.
```

### Examples

Here are some example natural language inputs and their corresponding commands:

| Natural Language | Generated Command |
|-----------------|-------------------|
| "list all files in current folder as a list" | `ls -al` |
| "push code" | `git push origin main` |
| "show disk usage" | `df -h` |
| "find all python files" | `find . -name "*.py"` |
| "show running processes" | `ps aux` |
| "create a new directory called test" | `mkdir test` |
| "download file from url" | `wget [url]` or `curl -O [url]` |
| "show git status" | `git status` |
| "compress folder into zip" | `zip -r folder.zip folder/` |
| "show network connections" | `netstat -an` |

## 🛠️ Command Line Options

```
borabora [OPTIONS] [COMMAND...]

Options:
  --config          Configure API key and settings
  --dry-run, -d     Show command without executing (default is to execute)
  --version, -v     Show version information
  --help, -h        Show help message
```

## 🔧 Configuration

Borabora stores its configuration in `~/.clai/config.json`. You can:

- Set API key: `borabora --config`
- Use environment variable: `GROQ_API_KEY`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository at [https://github.com/invisible-hand/borabora](https://github.com/invisible-hand/borabora)
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

- Always review generated commands before execution
- Borabora is powered by Groq AI and may occasionally generate incorrect commands
- Borabora executes commands by default after confirmation - use `--dry-run` for safety
- The tool is designed for common Unix/Linux commands and may not cover all edge cases

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/invisible-hand/borabora/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide as much detail as possible about your environment and the issue

## 🎯 Roadmap

- [ ] Support for more AI models
- [ ] Command history and favorites
- [ ] Interactive mode
- [ ] Plugin system for custom commands
- [ ] Shell integration (bash/zsh completions)
- [ ] Command explanation mode

---

Made with ❤️ by [AndreyZ](https://github.com/invisible-hand)
