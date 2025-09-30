# SuperGemini Framework Flags User Guide 🏁

## ✅ Verification Status
- **SuperGemini Version**: v4.0+ Compatible
- **Last Tested**: 2025-01-16
- **Test Environment**: Linux/Windows/macOS
- **Flag Syntax**: ✅ All Verified

## 🧪 Testing Your Flag Setup

Before using flags, verify they work correctly:

```bash
# Test basic flag recognition
/sg:analyze . --help
# Expected: Shows available flags without errors

# Test auto-flag activation
/sg:implement "test component"
# Expected: Magic + Context7 should auto-activate for UI requests

# Test manual flag override
/sg:analyze . --no-mcp
# Expected: Native execution only, no MCP servers
```

**If tests fail**: Check [Installation Guide](../Getting-Started/installation.md) for flag system setup

## 🤖 Most Flags Activate Automatically - Don't Stress About It!

SuperGemini's intelligent flag system automatically detects task complexity and context, then activates appropriate flags behind the scenes. You get optimized performance without memorizing flag combinations.

**Intelligent Auto-Activation**: Type `/sg:analyze large-codebase/` → `--introspect` + `--serena` + `--orchestrate` activate automatically. Type complex multi-file operations → `--task-manage` + `--delegate` optimize execution. Work under resource pressure → `--uc` compresses output.

**Manual Override Available**: When you want specific behavior, flags provide precise control. But in most cases, SuperGemini's automatic selection delivers optimal results.

---

## 🚀 Just Try These (No Flag Knowledge Required)

**Commands Work Great Without Flags:**
```bash
# These automatically get optimal flags
/sg:analyze "mobile fitness app"
# → Auto-activates: --introspect, --context7

/sg:analyze src/ --focus security  
# → Auto-activates: --introspect, --serena, --orchestrate

/sg:implement "user authentication system"
# → Auto-activates: --task-manage, --c7, --magic, --validate

/sg:troubleshoot "API performance issues"
# → Auto-activates: --introspect, --seq, --serena

/sg:improve legacy-code/ --focus maintainability
# → Auto-activates: --task-manage, --morph, --serena, --safe-mode
```

**Behind-the-Scenes Optimization:**
- **Context Analysis**: Keywords trigger appropriate specialists and tools
- **Complexity Detection**: Multi-file operations get coordination flags
- **Resource Awareness**: System load triggers efficiency optimizations
- **Quality Gates**: Risky operations automatically enable safety flags
- **Performance Tuning**: Optimal tool combinations selected automatically

**When Manual Flags Help:**
- Override automatic detection: `--no-mcp` for lightweight execution
- Force specific behavior: `--uc` for compressed output
- Learning and exploration: `--introspect` to see reasoning
- Resource control: `--concurrency 2` to limit parallel operations

---

## What Are Flags? 🤔

**Flags are Modifiers** that adjust SuperGemini's behavior for specific contexts and requirements:

**Flag Syntax:**
```bash
/sg:command [args] --flag-name [value]

# Examples
/sg:analyze src/ --focus security --depth deep
/sg:implement "auth" --task-manage --validate
/sg:troubleshoot issue/ --introspect --uc --concurrency 3
```

**Two Types of Activation:**
1. **Automatic** (90% of use): SuperGemini detects context and activates optimal flags
2. **Manual** (10% of use): You override or specify exact behavior needed

**Flag Functions:**
- **Behavioral Modes**: `--brainstorm`, `--introspect`, `--task-manage`
- **Tool Selection**: `--c7`, `--seq`, `--magic`, `--morph`, `--serena`, `--play`
- **Analysis Modes**: `--introspect`, `--task-manage`, `--orchestrate`
- **Efficiency Control**: `--uc`, `--concurrency`, `--scope`
- **Safety & Quality**: `--safe-mode`, `--validate`, `--dry-run`

**Auto-Activation vs Manual Override:**
- **Auto**: `/sg:implement "React dashboard"` → Magic + Context7 + task coordination
- **Manual**: `/sg:implement "simple function" --no-mcp` → Native-only execution

## Flag Categories 📂

### Planning & Analysis Flags 🧠

**Thinking Depth Control:**

**`--introspect`** - Standard Analysis (~4K tokens)
- **Auto-Triggers**: Multi-component analysis, moderate complexity
- **Manual Use**: Force structured thinking for simple tasks
- **Enables**: Sequential MCP for systematic reasoning

#### Success Criteria
- [ ] Sequential MCP server activates (check status output)
- [ ] Analysis follows structured methodology with clear sections
- [ ] Output includes evidence-based reasoning and conclusions
- [ ] Token usage approximately 4K or less

```bash
/sg:analyze auth-system/ --introspect
# → Structured analysis with evidence-based reasoning
```

**Verify:** Sequential MCP should show in status output  
**Test:** Output should have systematic structure with hypothesis testing  
**Check:** Analysis quality should be notably higher than basic mode

**`--introspect`** - Deep Analysis (~10K tokens)  
- **Auto-Triggers**: Architectural analysis, system-wide dependencies
- **Manual Use**: Force comprehensive analysis
- **Enables**: Sequential + Context7 for deep understanding
```bash
/sg:troubleshoot "performance degradation" --introspect
# → Comprehensive root cause analysis with framework patterns
```

**`--orchestrate`** - Maximum Analysis (~32K tokens)
- **Auto-Triggers**: Critical system redesign, legacy modernization
- **Manual Use**: Force maximum analytical depth
- **Enables**: All MCP servers for comprehensive capability
```bash
/sg:analyze enterprise-architecture/ --orchestrate
# → Maximum depth with all tools and reasoning capacity
```

**Mode Activation Flags:**

**``** / **`--bs`** - Interactive Discovery
- **Auto-Triggers**: Vague requests, exploration keywords
- **Manual Use**: Force collaborative requirement discovery
```bash
/sg:implement "better user experience"
# → Socratic questions to clarify requirements before implementation
```

**`--introspect`** - Reasoning Transparency
- **Auto-Triggers**: Error recovery, learning contexts
- **Manual Use**: Expose decision-making process for learning
```bash
/sg:analyze complex-algorithm/ --introspect
# → Transparent reasoning with 🤔, 🎯, ⚡ markers
```

### Efficiency & Control Flags ⚡

**Output Compression:**

**`--uc`** / **`--ultracompressed`** - Token Efficiency (30-50% reduction)
- **Auto-Triggers**: Context usage >75%, large operations, resource pressure
- **Manual Use**: Force compressed communication
- **Effect**: Symbol-enhanced output while preserving ≥95% information quality
```bash
/sg:analyze large-project/ --uc
# → "auth.js:45 → 🛡️ sec risk in user val()" vs verbose explanations
```

**`--token-efficient`** - Moderate Compression
- **Auto-Triggers**: Medium resource pressure, efficiency requirements
- **Manual Use**: Balance between detail and efficiency
```bash
/sg:troubleshoot "memory leak" --token-efficient
# → Structured but concise problem analysis
```

**Execution Control:**

**`--concurrency [n]`** - Parallel Operation Control (1-15)
- **Auto-Triggers**: Resource optimization needs
- **Manual Use**: Control system load and parallel processing
```bash
/sg:improve large-codebase/ --concurrency 3
# → Limit to 3 parallel operations for resource management
```

**`--scope [file|module|project|system]`** - Analysis Boundary
- **Auto-Triggers**: Analysis boundary detection
- **Manual Use**: Explicitly define operational scope
```bash
/sg:analyze src/auth/ --scope module
# → Focus analysis on authentication module only
```

**`--loop`** / **`--iterations [n]`** - Iterative Improvement
- **Auto-Triggers**: "polish", "refine", "enhance", "improve" keywords
- **Manual Use**: Force iterative improvement cycles
```bash
/sg:improve user-interface/ --loop --iterations 3
# → 3 improvement cycles with validation gates
```

### Focus & Specialization Flags 🎯

**Domain-Specific Analysis:**

**`--focus [domain]`** - Target Expertise Application
- **Available Domains**: `performance`, `security`, `quality`, `architecture`, `accessibility`, `testing`
- **Auto-Triggers**: Domain-specific keywords and file patterns
- **Manual Use**: Force specific analytical perspective

```bash
# Security-focused analysis
/sg:analyze payment-system/ --focus security
# → Security specialist + vulnerability assessment + compliance validation

# Performance optimization focus  
/sg:improve api-endpoints/ --focus performance
# → Performance engineer + bottleneck analysis + optimization patterns

# Architecture evaluation
/sg:analyze microservices/ --focus architecture
# → System architect + design pattern analysis + scalability assessment

# Quality improvement
/sg:review codebase/ --focus quality
# → Quality engineer + code smell detection + maintainability analysis
```

**Task Management:**

**`--task-manage`** / **`--delegate`** - Complex Coordination
- **Auto-Triggers**: >3 steps, >2 directories, >3 files
- **Manual Use**: Force hierarchical task organization for simple tasks
```bash
/sg:implement "simple feature" --task-manage
# → Phase-based approach with progress tracking even for simple tasks
```

**`--delegate [auto|files|folders]`** - Orchestration Strategy
- **Auto-Triggers**: >7 directories OR >50 files OR complexity >0.8
- **Manual Use**: Control delegation strategy
```bash
/sg:refactor enterprise-codebase/ --delegate folders
# → Delegate by directory structure for systematic organization
```

### Tool Integration Flags 🛠️

**MCP Server Control:**

**Individual Server Flags:**
- **`--c7`** / **`--context7`**: Documentation and framework patterns
- **`--seq`** / **`--sequential`**: Structured multi-step reasoning  
- **`--magic`**: Modern UI component generation
- **`--morph`** / **`--morphllm`**: Pattern-based code transformation
- **`--serena`**: Semantic understanding and project memory
- **`--play`** / **`--playwright`**: Browser automation and testing

```bash
# Specific server combinations
/sg:implement "dashboard" --magic --c7
# → UI generation + framework patterns

/sg:analyze complex-issue/ --seq --serena  
# → Structured reasoning + project context

/sg:improve legacy-code/ --morph --serena --seq
# → Pattern transformation + context + systematic analysis
```

**Server Group Control:**

**`--all-mcp`** - Maximum Capability
- **Auto-Triggers**: Maximum complexity scenarios, multi-domain problems
- **Manual Use**: Force all tools for comprehensive capability
```bash
/sg:implement "enterprise-platform" --all-mcp
# → All 6 MCP servers coordinated for maximum capability
```

**`--no-mcp`** - Native-Only Execution
- **Auto-Triggers**: Performance priority, simple tasks
- **Manual Use**: Force lightweight execution without MCP overhead
```bash
/sg:explain "simple function" --no-mcp
# → Fast native response without MCP server coordination
```

**Tool Optimization:**

**`--orchestrate`** - Intelligent Tool Selection
- **Auto-Triggers**: Multi-tool operations, performance constraints, >3 files
- **Manual Use**: Force optimal tool coordination
```bash
/sg:refactor components/ --orchestrate
# → Optimal tool selection and parallel execution coordination
```

### Safety & Validation Flags 🛡️

**Risk Management:**

**`--validate`** - Pre-execution Risk Assessment
- **Auto-Triggers**: Risk score >0.7, resource usage >75%, production environment
- **Manual Use**: Force validation gates for any operation
```bash
/sg:implement "payment-processing" --validate
# → Risk assessment + validation gates before implementation
```

**`--safe-mode`** - Maximum Conservative Execution
- **Auto-Triggers**: Resource usage >85%, production environment, critical operations
- **Manual Use**: Force maximum safety protocols
- **Auto-Enables**: `--uc` for efficiency, `--validate` for safety
```bash
/sg:improve production-database/ --safe-mode
# → Conservative execution + auto-backup + rollback planning
```

**Preview & Testing:**

**`--dry-run`** - Preview Without Execution
- **Manual Use**: Preview changes without applying them
```bash
/sg:cleanup legacy-code/ --dry-run
# → Show what would be cleaned up without making changes
```

**`--backup`** - Force Backup Creation
- **Auto-Triggers**: Risky operations, file modifications
- **Manual Use**: Ensure backup creation before operations
```bash
/sg:refactor critical-module/ --backup
# → Create backup before refactoring operations
```

**`--tests-required`** - Mandate Test Validation
- **Auto-Triggers**: Critical code changes, production modifications
- **Manual Use**: Force test execution before proceeding
```bash
/sg:improve auth-system/ --tests-required
# → Run tests and require passing before improvement application
```

### Execution Control Flags 🎛️

**Workflow Management:**

**`--parallel`** - Force Parallel Execution
- **Auto-Triggers**: Independent operations, >3 files, multi-tool scenarios
- **Manual Use**: Force parallel processing for eligible operations
```bash
/sg:analyze multiple-modules/ --parallel
# → Analyze modules concurrently instead of sequentially
```

**`--sequential`** - Force Sequential Execution  
- **Manual Use**: Override parallel processing for dependency reasons
```bash
/sg:implement "multi-step-feature" --sequential
# → Force step-by-step execution with dependencies
```

**Resource Control:**

**`--memory-limit [MB]`** - Memory Usage Control
- **Auto-Triggers**: Large operations, resource constraints
- **Manual Use**: Explicit memory management
```bash
/sg:analyze large-dataset/ --memory-limit 2048
# → Limit analysis to 2GB memory usage
```

**`--timeout [seconds]`** - Operation Timeout
- **Auto-Triggers**: Complex operations, MCP server timeouts
- **Manual Use**: Set explicit timeout boundaries
```bash
/sg:troubleshoot "complex-performance-issue" --timeout 300
# → 5-minute timeout for troubleshooting analysis
```

**Output Control:**

**`--format [text|json|html|markdown]`** - Output Format
- **Auto-Triggers**: Analysis export, documentation generation
- **Manual Use**: Specify exact output format
```bash
/sg:analyze api-performance/ --format json --export report.json
# → JSON-formatted analysis results for processing
```

**`--verbose`** / **`--quiet`** - Verbosity Control
- **Manual Use**: Override automatic verbosity decisions
```bash
/sg:build project/ --verbose
# → Detailed build output and progress information

/sg:test suite/ --quiet  
# → Minimal output, results only
```

## Common Flag Combinations 🔗

**Development Workflow Patterns:**

**Full Analysis & Improvement:**
```bash
/sg:analyze codebase/ --introspect --all-mcp --orchestrate
# → Deep analysis + all tools + optimal coordination
```

**Safe Production Changes:**
```bash
/sg:improve production-api/ --safe-mode --validate --backup --tests-required
# → Maximum safety protocols for production modifications
```

**Rapid Prototyping:**
```bash
/sg:implement "quick-feature" --magic --c7 --no-validate
# → Fast UI generation + patterns without safety overhead
```

**Large-Scale Refactoring:**
```bash
/sg:refactor legacy-system/ --task-manage --serena --morph --parallel --backup
# → Systematic coordination + context + transformation + safety
```

**Performance Investigation:**
```bash
/sg:troubleshoot "slow-performance" --introspect --focus performance --seq --play
# → Deep analysis + performance focus + reasoning + browser testing
```

**Learning & Understanding:**
```bash
/sg:analyze new-codebase/ --introspect --c7 --introspect
# → Transparent reasoning + discovery + documentation + analysis
```

**Resource-Constrained Environments:**
```bash
/sg:implement "feature" --uc --concurrency 1 --no-mcp --scope file
# → Compressed output + limited resources + lightweight execution
```

**Quality Assurance Workflow:**
```bash
/sg:review code-changes/ --focus quality --validate --tests-required --introspect
# → Quality analysis + validation + testing + structured reasoning
```

**Documentation Generation:**
```bash
/sg:document api/ --c7 --magic --format markdown --focus accessibility
# → Documentation patterns + UI examples + accessible format
```

**Complex Architecture Design:**
```bash
/sg:design "microservices-platform" --orchestrate --all-mcp --orchestrate
# → Maximum analysis + discovery + all tools + optimal coordination
```

## Flag Reference Quick Cards 📋

### 🧠 Analysis & Thinking Flags
| Flag | Purpose | Auto-Trigger | Token Impact |
|------|---------|--------------|--------------|
| `--introspect` | Standard analysis | Multi-component tasks | ~4K tokens |
| `--introspect` | Deep analysis | Architectural tasks | ~10K tokens |
| `--orchestrate` | Maximum analysis | Critical system work | ~32K tokens |
| `` | Interactive discovery | Vague requirements | Variable |
| `--introspect` | Reasoning transparency | Learning contexts | +10% detail |

### ⚡ Efficiency & Performance Flags  
| Flag | Purpose | Auto-Trigger | Performance Impact |
|------|---------|--------------|-------------------|
| `--uc` | Token compression | >75% context usage | 30-50% reduction |
| `--token-efficient` | Moderate compression | Resource pressure | 15-30% reduction |
| `--concurrency N` | Parallel control | Multi-file ops | +45% speed |
| `--orchestrate` | Tool optimization | Complex coordination | +30% efficiency |
| `--scope [level]` | Boundary control | Analysis scope | Focused execution |

### 🛠️ Tool Integration Flags
| Flag | MCP Server | Auto-Trigger | Best For |
|------|------------|--------------|----------|
| `--c7` / `--context7` | Context7 | Library imports | Documentation, patterns |
| `--seq` / `--sequential` | Sequential | Complex debugging | Systematic reasoning |
| `--magic` | Magic | UI requests | Component generation |
| `--morph` / `--morphllm` | Morphllm | Multi-file edits | Pattern transformation |
| `--serena` | Serena | Symbol operations | Project memory |
| `--play` / `--playwright` | Playwright | Browser testing | E2E automation |
| `--all-mcp` | All servers | Max complexity | Comprehensive capability |
| `--no-mcp` | None | Simple tasks | Lightweight execution |

### 🎯 Focus & Specialization Flags
| Flag | Domain | Expert Activation | Use Case |
|------|--------|------------------|----------|
| `--focus security` | Security | Security engineer | Vulnerability analysis |
| `--focus performance` | Performance | Performance engineer | Optimization |
| `--focus quality` | Quality | Quality engineer | Code review |
| `--focus architecture` | Architecture | System architect | Design analysis |
| `--focus accessibility` | Accessibility | UX specialist | Compliance validation |
| `--focus testing` | Testing | QA specialist | Test strategy |

### 🛡️ Safety & Control Flags
| Flag | Purpose | Auto-Trigger | Safety Level |
|------|---------|--------------|--------------|
| `--safe-mode` | Maximum safety | Production ops | Maximum |
| `--validate` | Risk assessment | High-risk ops | High |
| `--backup` | Force backup | File modifications | Standard |
| `--dry-run` | Preview only | Manual testing | Preview |
| `--tests-required` | Mandate testing | Critical changes | Validation |

### 📋 Workflow & Task Flags  
| Flag | Purpose | Auto-Trigger | Coordination |
|------|---------|--------------|--------------|
| `--task-manage` | Hierarchical organization | >3 steps | Phase-based |
| `--delegate [mode]` | Sub-task routing | >50 files | Intelligent routing |
| `--loop` | Iterative cycles | "improve" keywords | Quality cycles |
| `--iterations N` | Cycle count | Specific improvements | Controlled iteration |
| `--parallel` | Force concurrency | Independent ops | Performance |

## Advanced Flag Usage 🚀

### Context-Aware Flag Selection

**Adaptive Flagging Based on Project Type:**

**React/Frontend Projects:**
```bash
# Automatically optimized for React development
/sg:implement "user-dashboard" 
# → Auto-flags: --magic --c7 --focus accessibility --orchestrate

# Manual optimization for specific needs
/sg:implement "dashboard" --magic --c7 --play --focus accessibility
# → UI generation + patterns + testing + accessibility validation
```

**Backend/API Projects:**
```bash
# Automatically optimized for backend development  
/sg:implement "payment-api"
# → Auto-flags: --focus security --validate --c7 --seq

# Manual security-first approach
/sg:implement "api" --focus security --validate --backup --tests-required
# → Security analysis + validation + safety protocols
```

**Legacy Modernization:**
```bash
# Complex legacy work gets automatic coordination
/sg:improve legacy-monolith/
# → Auto-flags: --task-manage --serena --morph --introspect --backup

# Manual control for specific modernization strategy  
/sg:improve legacy/ --orchestrate --task-manage --serena --morph --safe-mode
# → Maximum analysis + coordination + transformation + safety
```

### Flag Precedence & Conflict Resolution

**Priority Hierarchy:**
1. **Safety First**: `--safe-mode` > `--validate` > optimization flags
2. **Explicit Override**: User flags > auto-detection  
3. **Depth Hierarchy**: `--orchestrate` > `--introspect` > `--task-manage`
4. **MCP Control**: `--no-mcp` overrides all individual MCP flags
5. **Scope Precedence**: `system` > `project` > `module` > `file`

**Conflict Resolution Examples:**
```bash
# Safety overrides efficiency
/sg:implement "critical-feature" --uc --safe-mode
# → Result: Safe mode wins, auto-enables backup and validation

# Explicit scope overrides auto-detection
/sg:analyze large-project/ --scope file target.js
# → Result: Only analyzes target.js despite project size

# No-MCP overrides individual server flags
/sg:implement "feature" --magic --c7 --no-mcp  
# → Result: No MCP servers used, native execution only
```

### Dynamic Flag Adaptation

**Resource-Responsive Flagging:**
```bash
# System automatically adapts based on available resources
/sg:analyze enterprise-codebase/
# → High resources: --all-mcp --parallel --introspect
# → Medium resources: --c7 --seq --serena --introspect  
# → Low resources: --no-mcp --uc --scope module
```

**Complexity-Driven Selection:**
```bash
# Flags scale with detected complexity
/sg:implement "simple helper function"
# → Auto-flags: minimal, fast execution

/sg:implement "microservices authentication"  
# → Auto-flags: --orchestrate --all-mcp --task-manage --validate --orchestrate
```

### Expert Flag Patterns

**Security-First Development:**
```bash
# Progressive security validation
/sg:implement "auth-system" --focus security --validate --tests-required
/sg:review "payment-code" --focus security --introspect --backup
/sg:analyze "user-data" --focus security --all-mcp --safe-mode
```

**Performance Optimization Workflow:**
```bash
# Systematic performance improvement
/sg:analyze --focus performance --introspect --seq --play
/sg:improve --focus performance --morph --parallel --validate  
/sg:test --focus performance --play --format json --export metrics.json
```

**Learning & Discovery Patterns:**
```bash
# Understanding complex systems
/sg:load new-codebase/ --introspect --serena
/sg:analyze architecture/ --introspect --c7 --all-mcp
/sg:explain concepts/ --introspect --c7 --focus accessibility
```

## Flag Troubleshooting 🔧

## 🚨 Quick Troubleshooting

### Common Issues (< 2 minutes)
- **Flag not recognized**: Check spelling and verify against `python3 -m SuperGemini --help`
- **MCP flag failures**: Check Node.js installation and server configuration
- **Auto-flags wrong**: Use manual override with `--no-mcp` or specific flags
- **Performance degradation**: Reduce complexity with `--scope file` or `--concurrency 1`
- **Flag conflicts**: Check flag priority rules and use single flags

### Immediate Fixes
- **Reset flags**: Remove all flags and let auto-detection work
- **Check compatibility**: Use `/sg:help flags` for valid combinations
- **Restart session**: Exit and restart Gemini CLI to reset flag state
- **Verify setup**: Run `SuperGemini status --flags` to check flag system

### Flag-Specific Troubleshooting

**Flag Not Recognized:**
```bash
# Problem: "Unknown flag --invalid-flag"
# Quick Fix: Check flag spelling and availability
/sg:help flags                         # List all valid flags
python3 -m SuperGemini --help flags    # System-level flag help
# Common typos: --brainstrom →, --seq → --sequential
```

**MCP Flag Issues:**
```bash
# Problem: --magic, --morph, --c7 not working
# Quick Fix: Check MCP server status
SuperGemini status --mcp              # Verify server connections
node --version                        # Ensure Node.js v16+
npm cache clean --force               # Clear package cache
/sg:command --no-mcp                  # Bypass MCP temporarily
```

**Flag Combination Conflicts:**
```bash
# Problem: "Flag conflict: --all-mcp and --no-mcp"
# Quick Fix: Use flag priority rules
/sg:command --no-mcp                  # --no-mcp overrides --all-mcp
/sg:command --orchestrate --introspect      # --orchestrate overrides --introspect
/sg:command --safe-mode --uc          # --safe-mode auto-enables --uc
```

**Auto-Detection Issues:**
```bash
# Problem: Wrong flags auto-activated
# Quick Fix: Manual override with explicit flags
/sg:analyze simple-file.js --no-mcp   # Override complex auto-detection
/sg:implement "basic function" --introspect # Force thinking mode
/sg:analyze clear-requirement       # Force discovery mode
```

### Performance-Related Flag Issues

**Resource Exhaustion:**
```bash
# Problem: System slowing down with --all-mcp --orchestrate
# Quick Fix: Reduce resource usage
/sg:command --c7 --seq                # Essential servers only
/sg:command --concurrency 1           # Limit parallel operations
/sg:command --scope file              # Reduce analysis scope
/sg:command --uc                      # Enable compression
```

**Timeout Issues:**
```bash
# Problem: Commands hanging with complex flags
# Quick Fix: Timeout and resource management
/sg:command --timeout 60              # Set explicit timeout
/sg:command --memory-limit 2048       # Limit memory usage
/sg:command --safe-mode               # Conservative execution
killall node                         # Reset hung MCP servers
```

### API Key and Dependency Issues

**Missing API Keys:**
```bash
# Problem: --magic or --morph flags fail with "API key required"
# Expected behavior: These services require paid subscriptions
export TWENTYFIRST_API_KEY="key"     # For --magic flag
export MORPH_API_KEY="key"           # For --morph flag
# Alternative: /sg:command --no-mcp to skip paid services
```

**Missing Dependencies:**
```bash
# Problem: MCP flags fail with "command not found"
# Quick Fix: Install missing dependencies
node --version                        # Check Node.js v16+
npm install -g npx                   # Ensure npx available
SuperGemini install --components mcp --force  # Reinstall MCP
```

### Error Code Reference

| Flag Error | Meaning | Quick Fix |
|------------|---------|-----------|
| **F001** | Unknown flag | Check spelling with `/sg:help flags` |
| **F002** | Flag conflict | Use priority rules or remove conflicting flags |
| **F003** | MCP server unavailable | Check `node --version` and server status |
| **F004** | API key missing | Set environment variables or use `--no-mcp` |
| **F005** | Resource limit exceeded | Use `--concurrency 1` or `--scope file` |
| **F006** | Timeout exceeded | Increase `--timeout` or reduce complexity |
| **F007** | Permission denied | Check file permissions or run with appropriate access |
| **F008** | Invalid combination | Refer to flag priority hierarchy |

### Progressive Support Levels

**Level 1: Quick Fix (< 2 min)**
- Remove problematic flags and try again
- Use `--no-mcp` to bypass MCP server issues
- Check basic flag spelling and syntax

**Level 2: Detailed Help (5-15 min)**
```bash
# Flag-specific diagnostics
SuperGemini diagnose --flags
/sg:help flags --verbose
cat ~/.gemini/logs/flag-system.log
# Test individual flags one at a time
```
- See [Common Issues Guide](../Reference/common-issues.md) for flag installation problems

**Level 3: Expert Support (30+ min)**
```bash
# Deep flag system analysis
SuperGemini validate-flags --all-combinations
strace -e trace=execve /sg:command --verbose 2>&1
# Check flag interaction matrix
# Review flag priority implementation
```
- See [Diagnostic Reference Guide](../Reference/diagnostic-reference.md) for system-level analysis

**Level 4: Community Support**
- Report flag issues at [GitHub Issues](https://github.com/SuperGemini-Org/SuperGemini_Framework/issues)
- Include flag combination that failed
- Describe expected vs actual behavior

### Success Validation

After applying flag fixes, test with:
- [ ] `/sg:help flags` (should list all available flags)
- [ ] `/sg:command --basic-flag` (should work without errors)
- [ ] `SuperGemini status --mcp` (MCP flags should work if servers connected)
- [ ] Flag combinations follow priority rules correctly
- [ ] Auto-detection works for simple commands

## Quick Troubleshooting (Legacy)
- **Flag not recognized** → Check spelling: `SuperGemini --help flags`
- **MCP flag fails** → Check server status: `SuperGemini status --mcp`
- **Auto-flags wrong** → Use manual override: `--no-mcp` or specific flags
- **Performance issues** → Reduce complexity: `--scope file` or `--concurrency 1`
- **Flag conflicts** → Check priority rules in documentation

### Common Issues & Solutions

**Flag Not Recognized:**
```bash
# Problem: Unknown flag error
/sg:analyze code/ --unknown-flag

# Solution: Check flag spelling and availability
SuperGemini --help flags
/sg:help --flags
```

**Conflicting Flags:**
```bash
# Problem: Contradictory flags
/sg:implement "feature" --all-mcp --no-mcp

# Solution: Use flag priority rules
# --no-mcp overrides --all-mcp (explicit override wins)
# Use: /sg:implement "feature" --no-mcp
```

**Resource Issues:**
```bash
# Problem: System overload with --all-mcp --orchestrate
/sg:analyze large-project/ --all-mcp --orchestrate

# Solution: Reduce resource usage
/sg:analyze large-project/ --c7 --seq --introspect --concurrency 2
# Or let auto-detection handle it: /sg:analyze large-project/
```

**MCP Server Connection Problems:**
```bash
# Problem: MCP flags not working
/sg:implement "dashboard" --magic  # Magic server not responding

# Solutions:
# 1. Check MCP installation
SuperGemini install --list-components | grep mcp

# 2. Restart Gemini CLI session (MCP connections refresh)
# 3. Use fallback approach
/sg:implement "dashboard" --no-mcp  # Native execution

# 4. Reinstall MCP servers
SuperGemini install --components mcp --force
```

**Performance Problems:**
```bash
# Problem: Slow execution with complex flags
/sg:analyze codebase/ --orchestrate --all-mcp --parallel

# Solutions:
# 1. Reduce complexity
/sg:analyze codebase/ --introspect --c7 --seq

# 2. Use scope limiting
/sg:analyze codebase/ --scope module --focus quality

# 3. Enable efficiency mode
/sg:analyze codebase/ --uc --concurrency 1
```

### Flag Debugging

**Check Auto-Activated Flags:**
```bash
# Add --verbose to see which flags were auto-activated
/sg:analyze project/ --verbose
# → Output shows: "Auto-activated: --introspect, --serena, --orchestrate"
```

**Test Flag Combinations:**
```bash
# Use --dry-run to test flag effects without execution
/sg:improve code/ --task-manage --morph --dry-run
# → Shows planned execution without making changes
```

**Validate Flag Usage:**
```bash
# Check flag compatibility
SuperGemini validate-flags --introspect --no-mcp --magic
# → Reports conflicts and suggests corrections
```

### Best Practices for Flag Usage

**Start Simple:**
1. **Trust Auto-Detection**: Let SuperGemini choose flags automatically
2. **Add Specific Flags**: Override only when you need specific behavior
3. **Use Common Patterns**: Start with proven flag combinations
4. **Monitor Performance**: Watch for resource usage and adjust accordingly

**Progressive Enhancement:**
```bash
# Week 1: Use commands without flags
/sg:analyze src/
/sg:implement "feature"

# Week 2: Add specific focus
/sg:analyze src/ --focus security
/sg:implement "feature" --magic

# Week 3: Combine for workflows  
/sg:analyze src/ --focus security --introspect
/sg:implement "feature" --magic --c7 --validate

# Month 2+: Advanced patterns
/sg:improve legacy/ --task-manage --serena --morph --safe-mode
```

**Flag Selection Strategy:**
1. **Purpose-First**: What do you want to achieve?
2. **Context-Aware**: Consider project type and complexity
3. **Resource-Conscious**: Monitor system load and adjust
4. **Safety-Minded**: Use validation flags for important changes
5. **Learning-Oriented**: Add `--introspect` when exploring

## Related Guides

**Learning Progression:**

**🌱 Essential (Week 1)**
- [Quick Start Guide](../Getting-Started/quick-start.md) - Experience auto-flagging naturally
- [Commands Reference](commands.md) - Commands automatically select optimal flags
- [Installation Guide](../Getting-Started/installation.md) - Flag system setup

**🌿 Intermediate (Week 2-3)**
- [Behavioral Modes](modes.md) - How flags activate behavioral modes
- [Agents Guide](agents.md) - Flag interaction with specialized agents  
- [MCP Servers](mcp-servers.md) - MCP server activation flags

**🌲 Advanced (Month 2+)**
- [Session Management](session-management.md) - Long-term flag patterns
- [Best Practices](../Reference/quick-start-practices.md) - Flag optimization strategies
- [Examples Cookbook](../Reference/examples-cookbook.md) - Real-world flag combinations

**🔧 Expert**
- [Technical Architecture](../Developer-Guide/technical-architecture.md) - Flag system implementation
- [Contributing Code](../Developer-Guide/contributing-code.md) - Extending flag capabilities

**Flag-Specific Learning Paths:**

**🎯 Focus Flags Mastery:**
- **Security**: `--focus security` → Security engineer activation
- **Performance**: `--focus performance` → Performance optimization patterns
- **Quality**: `--focus quality` → Code review and improvement workflows

**🧠 Analysis Depth Progression:**
- **Basic**: No flags → automatic detection
- **Structured**: `--introspect` → systematic analysis
- **Deep**: `--introspect` → comprehensive investigation  
- **Maximum**: `--orchestrate` → complete analytical capability

**🛠️ Tool Integration Journey:**
- **Single Tools**: `--c7`, `--magic` → specific capabilities
- **Combinations**: `--c7 --seq` → coordinated workflows
- **Full Suite**: `--all-mcp` → maximum capability
- **Optimization**: `--orchestrate` → intelligent coordination

**💡 Pro Tips:**
- **Start Without Flags**: Experience automatic optimization first
- **Add One at a Time**: Learn flag effects incrementally  
- **Use `--introspect`**: Understand decision-making process
- **Monitor Resources**: Watch system load and adjust accordingly
- **Save Patterns**: Document successful flag combinations for reuse
