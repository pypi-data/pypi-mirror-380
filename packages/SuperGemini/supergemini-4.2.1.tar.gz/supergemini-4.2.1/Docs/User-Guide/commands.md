# SuperGemini Commands Guide

> **Command Context**: This guide covers **Gemini CLI Commands** (`/sg:` commands). These run inside Gemini CLI chat, not in your terminal. For installation commands, see [Installation Guide](../Getting-Started/installation.md).

## ✅ Verification Status
- **SuperGemini Version**: v4.0+ Compatible
- **Last Tested**: 2025-01-16
- **Test Environment**: Linux/Windows/macOS
- **Command Syntax**: ✅ All Verified

> **Quick Start**: Try `/sg:analyze "your project idea"` → `/sg:implement "feature name"` → `/sg:test` to experience the core workflow.

## 🧪 Testing Your Setup

### 🖥️ Terminal Verification (Run in Terminal/CMD)
```bash
# Verify SuperGemini is working
SuperGemini --version
# Expected: SuperGemini Framework v4.0+

# Check MCP server connectivity
SuperGemini status --mcp
# Expected: At least context7 and sequential connected
```

### 💬 Gemini CLI Testing (Type in Gemini CLI Chat)
```
# Test basic /sg: command
/sg:analyze "test project"
# Expected: Interactive requirements discovery starts

# Test command help
/sg:help
# Expected: List of available commands
```

**If tests fail**: Check [Installation Guide](../Getting-Started/installation.md) or [Troubleshooting](#troubleshooting)

### 📋 Command Quick Reference

| Command Type | Where to Run | Format | Purpose |
|-------------|--------------|--------|---------|
| **🖥️ Installation** | Terminal/CMD | `SuperGemini [command]` | Setup and maintenance |
| **🔧 Configuration** | Terminal/CMD | `python3 -m SuperGemini` | Advanced configuration |
| **💬 Development** | Gemini CLI | `/sg:[command]` | AI-enhanced development |
| **⚡ Workflow** | Gemini CLI | `/sg:[command] --flags` | Enhanced automation |

> **Remember**: All `/sg:` commands work inside Gemini CLI chat, not your terminal.

## Table of Contents

- [Essential Commands](#essential-commands) - Start here (8 core commands)
- [Common Workflows](#common-workflows) - Command combinations that work
- [Full Command Reference](#full-command-reference) - All 21 commands organized by category
- [Troubleshooting](#troubleshooting) - Common issues and solutions
- [Command Index](#command-index) - Find commands by category

---

## Essential Commands

**Start with these 7 core commands for immediate productivity:**

> **Note on brainstorming functionality has been removed. Use `/sg:analyze` for comprehensive analysis and exploration.

### `/sg:implement` - Feature Development  
**Purpose**: Full-stack feature implementation with intelligent specialist routing  
**Syntax**: `/sg:implement "feature description"` `[--type frontend|backend|fullstack] [--focus security|performance]`  
**Auto-Activation**: Context-dependent specialists (Frontend, Backend, Security), Context7 + Magic MCP  

#### Success Criteria
- [ ] Command activates appropriate domain specialists
- [ ] Generates functional, production-ready code
- [ ] Includes basic error handling and validation
- [ ] Follows project conventions and patterns

**Use Cases**:
- Authentication: `/sg:implement "JWT login system"` → Security specialist + validation
- UI components: `/sg:implement "responsive dashboard"` → Frontend + Magic MCP  
- APIs: `/sg:implement "REST user endpoints"` → Backend + Context7 patterns
- Database: `/sg:implement "user schema with relationships"` → Database specialist

**Examples**:
```bash
/sg:implement "user registration with email verification"  # → Full auth flow
/sg:implement "payment integration" --focus security       # → Secure payment system
```

**Verify:** Code should compile/run without immediate errors  
**Test:** `/sg:implement "hello world function"` should produce working code  
**Check:** Security specialist should activate for auth-related implementations

### `/sg:analyze` - Code Assessment
**Purpose**: Comprehensive code analysis across quality, security, and performance  
**Syntax**: `/sg:analyze [path]` `[--focus quality|security|performance|architecture]`  
**Auto-Activation**: Analyzer specialist + domain experts based on focus  
**Use Cases**:
- Project health: `/sg:analyze .` → Overall assessment
- Security audit: `/sg:analyze --focus security` → Vulnerability report  
- Performance review: `/sg:analyze --focus performance` → Bottleneck identification
- Architecture review: `/sg:analyze --focus architecture` → Design patterns analysis

**Examples**:
```bash
/sg:analyze src/                        # → Quality + security + performance report
/sg:analyze --focus security --depth deep  # → Detailed security audit
```

### `/sg:troubleshoot` - Problem Diagnosis
**Purpose**: Systematic issue diagnosis with root cause analysis  
**Syntax**: `/sg:troubleshoot "issue description"` `[--type build|runtime|performance]`  
**Auto-Activation**: Analyzer + DevOps specialists, Sequential MCP for systematic debugging  
**Use Cases**:
- Runtime errors: `/sg:troubleshoot "500 error on login"` → Error investigation
- Build failures: `/sg:troubleshoot --type build` → Compilation issues  
- Performance problems: `/sg:troubleshoot "slow page load"` → Performance analysis
- Integration issues: `/sg:troubleshoot "API timeout errors"` → Connection diagnosis

**Examples**:
```bash
/sg:troubleshoot "users can't login"    # → Systematic auth flow analysis
/sg:troubleshoot --type build --fix     # → Build errors + suggested fixes
```

### `/sg:test` - Quality Assurance
**Purpose**: Comprehensive testing with coverage analysis  
**Syntax**: `/sg:test` `[--type unit|integration|e2e] [--coverage] [--fix]`  
**Auto-Activation**: QA specialist, Playwright MCP for E2E testing  
**Use Cases**:
- Full test suite: `/sg:test --coverage` → All tests + coverage report
- Unit testing: `/sg:test --type unit --watch` → Continuous unit tests
- E2E validation: `/sg:test --type e2e` → Browser automation tests  
- Test fixing: `/sg:test --fix` → Repair failing tests

**Examples**:
```bash
/sg:test --coverage --report            # → Complete test run with coverage
/sg:test --type e2e --browsers chrome,firefox  # → Cross-browser testing
```

### `/sg:improve` - Code Enhancement  
**Purpose**: Apply systematic code improvements and optimizations  
**Syntax**: `/sg:improve [path]` `[--type performance|quality|security] [--preview]`  
**Auto-Activation**: Analyzer specialist, Morphllm MCP for pattern-based improvements  
**Use Cases**:
- General improvements: `/sg:improve src/` → Code quality enhancements
- Performance optimization: `/sg:improve --type performance` → Speed improvements  
- Security hardening: `/sg:improve --type security` → Security best practices
- Refactoring: `/sg:improve --preview --safe-mode` → Safe code refactoring

**Examples**:
```bash
/sg:improve --type performance --measure-impact  # → Performance optimizations
/sg:improve --preview --backup           # → Preview changes before applying
```

### `/sg:document` - Documentation Generation
**Purpose**: Generate comprehensive documentation for code and APIs  
**Syntax**: `/sg:document [path]` `[--type api|user-guide|technical] [--format markdown|html]`  
**Auto-Activation**: Documentation specialist  
**Use Cases**:
- API docs: `/sg:document --type api` → OpenAPI/Swagger documentation  
- User guides: `/sg:document --type user-guide` → End-user documentation
- Technical docs: `/sg:document --type technical` → Developer documentation
- Inline comments: `/sg:document src/ --inline` → Code comments

**Examples**:
```bash
/sg:document src/api/ --type api --format openapi  # → API specification
/sg:document --type user-guide --audience beginners  # → User documentation
```

### `/sg:workflow` - Implementation Planning
**Purpose**: Generate structured implementation plans from requirements  
**Syntax**: `/sg:workflow "feature description"` `[--strategy agile|waterfall] [--format markdown]`  
**Auto-Activation**: Architect + Project Manager specialists, Sequential MCP  
**Use Cases**:
- Feature planning: `/sg:workflow "user authentication"` → Implementation roadmap
- Sprint planning: `/sg:workflow --strategy agile` → Agile task breakdown  
- Architecture planning: `/sg:workflow "microservices migration"` → Migration strategy
- Timeline estimation: `/sg:workflow --detailed --estimates` → Time and resource planning

**Examples**:
```bash
/sg:workflow "real-time chat feature"    # → Structured implementation plan
/sg:workflow "payment system" --strategy agile  # → Sprint-ready tasks
```

---

## Common Workflows

**Proven command combinations for common development scenarios:**

### New Project Setup
```bash
/sg:analyze "project concept"  # Define requirements
→ /sg:design "system architecture"       # Create technical design  
→ /sg:workflow "implementation plan"     # Generate development roadmap
→ /sg:save "project-plan"               # Save session context
```

### Feature Development
```bash
/sg:load "project-context"              # Load existing project
→ /sg:implement "feature name"          # Build the feature
→ /sg:test --coverage                   # Validate with tests
→ /sg:document --type api               # Generate documentation  
```

### Code Quality Improvement
```bash
/sg:analyze --focus quality             # Assess current state
→ /sg:cleanup --comprehensive           # Clean technical debt
→ /sg:improve --preview                 # Preview improvements
→ /sg:test --coverage                   # Validate changes
```

### Bug Investigation
```bash
/sg:troubleshoot "issue description"    # Diagnose the problem
→ /sg:analyze --focus problem-area      # Deep analysis of affected code
→ /sg:improve --fix --safe-mode         # Apply targeted fixes
→ /sg:test --related-tests              # Verify resolution
```

### Pre-Production Checklist  
```bash
/sg:analyze --focus security            # Security audit
→ /sg:test --type e2e --comprehensive   # Full E2E validation
→ /sg:build --optimize --target production  # Production build
→ /sg:document --type deployment        # Deployment documentation
```

---

## Full Command Reference

### Development Commands

| Command | Purpose | Auto-Activation | Best For |
|---------|---------|-----------------|----------|
| **workflow** | Implementation planning | Architect + PM, Sequential | Project roadmaps, sprint planning |
| **implement** | Feature development | Context specialists, Context7 + Magic | Full-stack features, API development |
| **build** | Project compilation | DevOps specialist | CI/CD, production builds |
| **design** | System architecture | Architect + UX, diagrams | API specs, database schemas |

#### `/sg:build` - Project Compilation
**Purpose**: Build and package projects with error handling  
**Syntax**: `/sg:build` `[--optimize] [--target production] [--fix-errors]`  
**Examples**: Production builds, dependency management, build optimization  
**Common Issues**: Missing deps → auto-install, memory issues → optimized parameters

#### `/sg:design` - System Architecture  
**Purpose**: Create technical designs and specifications  
**Syntax**: `/sg:design "system description"` `[--type api|database|system] [--format openapi|mermaid]`  
**Examples**: API specifications, database schemas, component architecture  
**Output Formats**: Markdown, Mermaid diagrams, OpenAPI specs, ERD

### Analysis Commands

| Command | Purpose | Auto-Activation | Best For |
|---------|---------|-----------------|----------|
| **analyze** | Code assessment | Analyzer + domain experts | Quality audits, security reviews |
| **troubleshoot** | Problem diagnosis | Analyzer + DevOps, Sequential | Bug investigation, performance issues |
| **explain** | Code explanation | Educational focus | Learning, code reviews |

#### `/sg:explain` - Code & Concept Explanation
**Purpose**: Educational explanations with progressive detail  
**Syntax**: `/sg:explain "topic or file"` `[--level beginner|intermediate|expert]`  
**Examples**: Code walkthroughs, concept clarification, pattern explanation  
**Teaching Styles**: Code-walkthrough, concept, pattern, comparison, tutorial

### Quality Commands

| Command | Purpose | Auto-Activation | Best For |
|---------|---------|-----------------|----------|
| **improve** | Code enhancement | Analyzer, Morphllm | Performance optimization, refactoring |
| **cleanup** | Technical debt | Analyzer, Morphllm | Dead code removal, organization |
| **test** | Quality assurance | QA specialist, Playwright | Test automation, coverage analysis |
| **document** | Documentation | Documentation specialist | API docs, user guides |

#### `/sg:cleanup` - Technical Debt Reduction
**Purpose**: Remove dead code and optimize project structure  
**Syntax**: `/sg:cleanup` `[--type imports|dead-code|formatting] [--confirm-before-delete]`  
**Examples**: Import optimization, file organization, dependency cleanup  
**Operations**: Dead code removal, import sorting, style formatting, file organization

### Project Management Commands

| Command | Purpose | Auto-Activation | Best For |
|---------|---------|-----------------|----------|
| **estimate** | Project estimation | Project Manager | Timeline planning, resource allocation |
| **task** | Task management | PM, Serena | Complex workflows, task tracking |
| **spawn** | Meta-orchestration | PM + multiple specialists | Large-scale projects, parallel execution |

#### `/sg:estimate` - Project Estimation
**Purpose**: Development estimates with complexity analysis  
**Syntax**: `/sg:estimate "project description"` `[--detailed] [--team-size N]`  
**Features**: Time estimates, complexity analysis, resource allocation, risk assessment  
**Stability**: 🌱 Growing - Improving estimation accuracy with each release

#### `/sg:task` - Project Management  
**Purpose**: Complex task workflow management  
**Syntax**: `/sg:task "task description"` `[--breakdown] [--priority high|medium|low]`  
**Features**: Task breakdown, priority management, cross-session tracking, dependency mapping  
**Stability**: 🌱 Growing - Enhanced delegation patterns being refined

#### `/sg:spawn` - Meta-System Orchestration
**Purpose**: Large-scale project orchestration with parallel execution  
**Syntax**: `/sg:spawn "complex project"` `[--parallel] [--monitor]`  
**Features**: Workflow orchestration, parallel execution, progress monitoring, resource management  
**Stability**: 🌱 Growing - Advanced orchestration capabilities under development

### Utility Commands

| Command | Purpose | Auto-Activation | Best For |
|---------|---------|-----------------|----------|
| **git** | Version control | DevOps specialist | Commit management, branch strategies |
| **index** | Command discovery | Context analysis | Exploring capabilities, finding commands |

#### `/sg:git` - Version Control
**Purpose**: Intelligent Git operations with smart commit messages  
**Syntax**: `/sg:git [operation]` `[--smart-messages] [--conventional]`  
**Features**: Smart commit messages, branch management, conflict resolution, workflow optimization  
**Stability**: ✅ Reliable - Proven commit message generation and workflow patterns

#### `/sg:index` - Command Discovery  
**Purpose**: Explore available commands and capabilities  
**Syntax**: `/sg:index` `[--category development|quality] [--search "keyword"]`  
**Features**: Command discovery, capability exploration, contextual recommendations, usage patterns  
**Stability**: 🧪 Testing - Command categorization and search being refined

### Session Commands

| Command | Purpose | Auto-Activation | Best For |
|---------|---------|-----------------|----------|
| **load** | Context loading | Context analysis, Serena | Session initialization, project onboarding |
| **save** | Session persistence | Session management, Serena | Checkpointing, context preservation |
| **reflect** | Task validation | Context analysis, Serena | Progress assessment, completion validation |
| **select-tool** | Tool optimization | Meta-analysis, all MCP | Performance optimization, tool selection |

#### `/sg:load` - Session Context Loading
**Purpose**: Initialize project context and session state  
**Syntax**: `/sg:load [path]` `[--focus architecture|codebase] [--session "name"]`  
**Features**: Project structure analysis, context restoration, session initialization, intelligent onboarding  
**Stability**: 🔧 Functional - Core loading works, advanced context analysis improving

#### `/sg:save` - Session Persistence
**Purpose**: Save session context and progress  
**Syntax**: `/sg:save "session-name"` `[--checkpoint] [--description "details"]`  
**Features**: Session checkpointing, context preservation, progress tracking, cross-session continuity  
**Stability**: 🔧 Functional - Basic persistence reliable, advanced features being enhanced

#### `/sg:reflect` - Task Reflection & Validation
**Purpose**: Analyze completion status and validate progress  
**Syntax**: `/sg:reflect` `[--type completion|progress] [--task "task-name"]`  
**Features**: Progress analysis, completion validation, quality assessment, next steps recommendation  
**Stability**: 🌱 Growing - Analysis patterns being refined for better insights

#### `/sg:select-tool` - Intelligent Tool Selection
**Purpose**: Optimize MCP tool selection based on complexity analysis  
**Syntax**: `/sg:select-tool "operation description"` `[--analyze-complexity] [--recommend]`  
**Features**: Complexity analysis, tool recommendation, MCP coordination, optimization strategies, resource planning  
**Stability**: 🌱 Growing - Tool selection algorithms being optimized

---

## Command Index

### By Category

**🚀 Project Initiation**
- Discovery mode - Activated through exploratory prompts
- `design` - System architecture  
- `workflow` - Implementation planning

**⚡ Development**  
- `implement` - Feature development
- `build` - Project compilation
- `git` - Version control

**🔍 Analysis & Quality**
- `analyze` - Code assessment
- `troubleshoot` - Problem diagnosis  
- `explain` - Code explanation
- `improve` - Code enhancement
- `cleanup` - Technical debt
- `test` - Quality assurance

**📝 Documentation**
- `document` - Documentation generation

**📊 Project Management**
- `estimate` - Project estimation
- `task` - Task management  
- `spawn` - Meta-orchestration

**🧠 Session & Intelligence**
- `load` - Context loading
- `save` - Session persistence
- `reflect` - Task validation
- `select-tool` - Tool optimization

**🔧 Utility**
- `index` - Command discovery

### By Maturity Level

**🔥 Production Ready** (Consistent, reliable results)
- `analyze`, `implement`, `troubleshoot`, `workflow`

**✅ Reliable** (Well-tested, stable features)  
- `workflow`, `design`, `test`, `document`, `git`

**🔧 Functional** (Core features work, enhancements ongoing)
- `improve`, `cleanup`, `build`, `load`, `save`

**🌱 Growing** (Rapid improvement, usable but evolving)
- `spawn`, `task`, `estimate`, `reflect`, `select-tool`

**🧪 Testing** (Experimental features, feedback welcome)
- `index`, `explain`

---

## 🚨 Quick Troubleshooting

### Common Issues (< 2 minutes)
- **Command not found**: Check `/sg:` prefix and SuperGemini installation
- **Invalid flag**: Verify flag against `python3 -m SuperGemini --help`
- **MCP server error**: Check Node.js installation and server configuration
- **Permission denied**: Run `chmod +x` or check file permissions

### Immediate Fixes
- **Reset session**: `/sg:load` to reinitialize
- **Clear cache**: Remove `~/.gemini/cache/` directory
- **Restart Gemini CLI**: Exit and restart application
- **Check status**: `python3 -m SuperGemini --version`

## Troubleshooting

### Command-Specific Issues

**Command Not Recognized:**
```bash
# Problem: "/sg:analyze not found"
# Quick Fix: Check command spelling and prefix
/sg:help commands  # List all available commands
python3 -m SuperGemini --help  # Verify installation
```

**Command Hangs or No Response:**
```bash
# Problem: Command starts but never completes
# Quick Fix: Check for dependency issues
/sg:command --timeout 30  # Set explicit timeout
/sg:command --no-mcp     # Try without MCP servers
ps aux | grep SuperGemini  # Check for hung processes
```

**Invalid Flag Combinations:**
```bash
# Problem: "Flag conflict detected"
# Quick Fix: Check flag compatibility
/sg:help flags            # List valid flags
/sg:command --help        # Command-specific flags
# Use simpler flag combinations or single flags
```

### MCP Server Issues

**Server Connection Failures:**
```bash
# Problem: MCP servers not responding
# Quick Fix: Verify server status and restart
SuperGemini status --mcp                    # Check all servers
/sg:command --no-mcp                       # Bypass MCP temporarily
node --version                             # Verify Node.js v16+
npm cache clean --force                    # Clear NPM cache
```

**Magic/Morphllm API Key Issues:**
```bash
# Problem: "API key required" errors
# Expected: These servers need paid API keys
export TWENTYFIRST_API_KEY="your_key"     # For Magic
export MORPH_API_KEY="your_key"           # For Morphllm
# Or use: /sg:command --no-mcp to skip paid services
```

### Performance Issues

**Slow Command Execution:**
```bash
# Problem: Commands taking >30 seconds
# Quick Fix: Reduce scope and complexity
/sg:command --scope file               # Limit to single file
/sg:command --concurrency 1           # Reduce parallel ops
/sg:command --uc                      # Use compressed output
/sg:command --no-mcp                  # Native execution only
```

**Memory/Resource Exhaustion:**
```bash
# Problem: System running out of memory
# Quick Fix: Resource management
/sg:command --memory-limit 1024       # Limit to 1GB
/sg:command --scope module            # Reduce analysis scope
/sg:command --safe-mode               # Conservative execution
killall node                         # Reset MCP servers
```

### Error Code Reference

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| **E001** | Command syntax error | Check command spelling and `/sg:` prefix |
| **E002** | Flag not recognized | Verify flag with `/sg:help flags` |
| **E003** | MCP server connection failed | Check Node.js and run `npm cache clean --force` |
| **E004** | Permission denied | Check file permissions or run with appropriate access |
| **E005** | Timeout exceeded | Reduce scope with `--scope file` or increase `--timeout` |
| **E006** | Memory limit exceeded | Use `--memory-limit` or `--scope module` |
| **E007** | Invalid project structure | Verify you're in a valid project directory |
| **E008** | Dependency missing | Check installation with `SuperGemini --version` |

### Progressive Support Levels

**Level 1: Quick Fix (< 2 min)**
- Use the Common Issues section above
- Try immediate fixes like restart or flag changes
- Check basic installation and dependencies

**Level 2: Detailed Help (5-15 min)**
```bash
# Comprehensive diagnostics
SuperGemini diagnose --verbose
/sg:help troubleshoot
cat ~/.gemini/logs/superclaude.log | tail -50
```
- See [Common Issues Guide](../Reference/common-issues.md) for detailed troubleshooting

**Level 3: Expert Support (30+ min)**
```bash
# Deep system analysis
SuperGemini diagnose --full-system
strace -e trace=file /sg:command 2>&1 | grep ENOENT
lsof | grep SuperGemini
# Check GitHub Issues for known problems
```
- See [Diagnostic Reference Guide](../Reference/diagnostic-reference.md) for advanced procedures

**Level 4: Community Support**
- Report issues at [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues)
- Include diagnostic output from Level 3
- Describe steps to reproduce the problem

### Success Validation

After applying fixes, test with:
- [ ] `python3 -m SuperGemini --version` (should show version)
- [ ] `/sg:analyze README.md` (should complete without errors)
- [ ] Check MCP servers respond: `SuperGemini status --mcp`
- [ ] Verify flags work: `/sg:help flags`
- [ ] Test basic workflow: `/sg:analyze "test"` → should provide analysis

## Quick Troubleshooting (Legacy)
- **Command not found** → Check installation: `SuperGemini --version`
- **Flag error** → Verify against [FLAGS.md](flags.md)  
- **MCP error** → Check server configuration: `SuperGemini status --mcp`
- **No output** → Restart Gemini CLI session
- **Slow performance** → Use `--scope file` or `--no-mcp`

### Common Issues

**Command Not Recognized**
```bash
# Check SuperGemini installation
SuperGemini --version

# Verify component installation  
SuperGemini install --list-components

# Restart Gemini CLI session
```

**Slow Performance**
```bash
# Limit analysis scope
/sg:analyze src/ --scope file

# Use specific MCP servers only
/sg:implement "feature" --c7 --seq  # Instead of --all-mcp

# Reduce concurrency
/sg:improve . --concurrency 2
```

**MCP Server Connection Issues**
```bash
# Check server status
ls ~/.gemini/.gemini.json

# Reinstall MCP components
SuperGemini install --components mcp --force

# Use native execution fallback
/sg:analyze . --no-mcp
```

**Scope Management Issues**
```bash
# Control analysis depth
/sg:analyze . --scope project  # Instead of system-wide

# Focus on specific areas
/sg:analyze --focus security   # Instead of comprehensive

# Preview before execution
/sg:improve . --dry-run --preview
```

### Error Recovery Patterns

**Build Failures**
```bash
/sg:troubleshoot --type build --verbose
→ /sg:build --fix-errors --deps-install
→ /sg:test --smoke  # Quick validation
```

**Test Failures**  
```bash
/sg:analyze --focus testing  # Identify test issues
→ /sg:test --fix --preview   # Preview test fixes
→ /sg:test --coverage        # Verify repairs
```

**Memory/Resource Issues**
```bash
/sg:select-tool "task" --analyze-complexity  # Check resource needs
→ /sg:task "subtask" --scope module          # Break into smaller pieces  
→ /sg:spawn "large-task" --parallel --concurrency 2  # Controlled parallelism
```

---

## Getting Help

**In-Session Help**
- `/sg:index --help` - Command discovery and help
- `/sg:explain "command-name"` - Detailed command explanation  
- `/sg:analyze --strategy systematic` - Systematic problem exploration

**Documentation**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Essential setup and first steps
- [Best Practices](../Reference/quick-start-practices.md) - Optimization and workflow patterns
- [Examples Cookbook](../Reference/examples-cookbook.md) - Real-world usage patterns

**Community Support**
- [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues) - Bug reports and feature requests
- [Discussions](https://github.com/SuperGemini-Org/SuperGemini_Framework/discussions) - Community help and patterns

---

## 🎯 Comprehensive Testing Procedures

### Essential Commands Verification
Run these tests to ensure all essential commands work correctly:

```bash
# Test 1: Discovery and Planning
/sg:analyze "test mobile app"
# Expected: 3-5 discovery questions about users, features, platform

# Test 2: Implementation  
/sg:implement "simple hello function"
# Expected: Working code that compiles/runs without errors

# Test 3: Analysis
/sg:analyze . --focus quality
# Expected: Quality assessment with specific recommendations

# Test 4: Troubleshooting
/sg:troubleshoot "simulated performance issue"
# Expected: Systematic investigation approach with hypotheses

# Test 5: Testing
/sg:test --coverage
# Expected: Test execution or test planning with coverage analysis

# Test 6: Code Enhancement
/sg:improve README.md --preview
# Expected: Improvement suggestions with preview of changes

# Test 7: Documentation
/sg:document . --type api
# Expected: API documentation or documentation planning

# Test 8: Workflow Planning
/sg:workflow "user authentication feature"
# Expected: Structured implementation plan with phases
```

### Success Benchmarks
- **Response Time**: Commands should respond within 10 seconds
- **Accuracy**: Domain specialists should activate for relevant requests
- **Completeness**: Outputs should include actionable next steps
- **Consistency**: Similar requests should produce consistent approaches

### Performance Validation
```bash
# Test resource usage
time /sg:analyze large-project/
# Expected: Completion within reasonable time based on project size

# Test MCP coordination
/sg:implement "React component" --verbose
# Expected: Magic + Context7 activation visible in output

# Test flag override
/sg:analyze . --no-mcp
# Expected: Native execution only, faster response
```

---

**Remember**: SuperGemini learns from your usage patterns. Start with the [Essential Commands](#essential-commands), explore [Common Workflows](#common-workflows), and gradually discover advanced capabilities. Use `/sg:index` whenever you need guidance.

