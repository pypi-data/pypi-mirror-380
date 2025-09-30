# 🤖 ASTODOJO Agent Helper

**Hello AI Agent!** This guide teaches you how to use ASTODOJO effectively. ASTODOJO is designed specifically for AI coding assistants like you to analyze Python codebases intelligently.

## 🔍 SCANNING OPERATIONS

### Basic Scan
**Command:** `astodojo scan`
**Arguments:**
- `path` (optional): File or directory to scan (defaults to current directory)
- `--format`: Output format - "tree", "json", "report"
- `--exclude`: Glob patterns to exclude files/directories

**Outcomes:**
- Tree format: Human-readable colored output with file structure
- JSON format: Structured data array for machine processing
- Report format: Statistical summary of findings

### Targeted Scan
**Command:** `astodojo scan [path]`
**Arguments:**
- `path`: Specific file, directory, or glob pattern
- `--exclude`: Skip certain files/patterns
- `--format`: Choose output format

**Outcomes:**
- Precise analysis of selected codebase sections
- Filtered results excluding unwanted files
- Context-aware TODO detection

## 📋 CONFIGURATION MANAGEMENT

### Initialize Config
**Command:** `astodojo init`
**Arguments:**
- `--directory`: Target directory for config file

**Outcomes:**
- Creates `.astodojorc` configuration file
- Sets up default exclude patterns
- Establishes project-specific settings

### Configuration Parameters
**File:** `.astodojorc`
**Key Parameters:**
- `exclude_patterns`: Array of glob patterns to ignore
- `output_format`: Default display format
- `colors`: Tag-specific color mappings
- `github_token`: GitHub API authentication
- `github_repo`: Target repository identifier

**Outcomes:**
- Persistent project configuration
- Automated exclusion of irrelevant files
- Consistent output formatting

## 🔗 GITHUB INTEGRATION

### Authentication Setup
**Automatic Process:**
- Run any GitHub command without credentials
- Browser opens to GitHub token creation
- Follows guided token setup process

**Required Environment:**
- `GITHUB_TOKEN`: Personal access token with repo scope
- `GITHUB_REPOSITORY`: Owner/repo format identifier

### Report Generation
**Command:** `astodojo github-report`
**Arguments:**
- `path` (optional): Directory to analyze
- `--format`: Output format preference

**Outcomes:**
- Synchronization recommendations
- Issue creation suggestions
- Current vs. new TODO comparison

### Issue Synchronization
**Command:** `astodojo github-sync`
**Arguments:**
- `--tag`: Specific tag type to sync (BLAME, TODO, BUG, etc.)
- `--count`: Maximum issues to create per run
- `path` (optional): Target directory scope

**Outcomes:**
- GitHub issues created from TODO items
- Controlled batch processing
- Links back to source code locations

## 📊 DATA STRUCTURES

### JSON Output Schema
**Structure:** Array of TODO objects
**Object Properties:**
- `file_path`: String - Relative file location
- `line_number`: Integer - Line position
- `tag`: String - TODO category (TODO, BLAME, BUG, etc.)
- `content`: String - TODO description text
- `parent_function`: String/Null - Containing function name
- `parent_class`: String/Null - Containing class name

**Outcomes:**
- Machine-readable TODO extraction
- Precise location tracking
- Contextual relationship mapping

## 🏷️ TODO TAG SYSTEM

### BLAME Tags
**Purpose:** Critical issues requiring human review
**Characteristics:**
- Security vulnerabilities
- Complex business logic
- Architectural decisions
- Performance-critical code

**Agent Response:** Always escalate to human developers

### TODO Tags
**Purpose:** General implementation tasks
**Characteristics:**
- Feature additions
- Code improvements
- Refactoring opportunities
- Missing functionality

**Agent Response:** Evaluate implementation complexity

### DEV-CRUFT Tags
**Purpose:** Temporary or debug code to remove
**Characteristics:**
- Debug print statements
- Temporary scaffolding
- Commented-out code blocks
- Development artifacts

**Agent Response:** Safe to remove automatically

### BUG Tags
**Purpose:** Confirmed code defects
**Characteristics:**
- Runtime errors
- Logic flaws
- Incorrect implementations
- Test failures

**Agent Response:** High priority fixes

### PAY-ATTENTION Tags
**Purpose:** Critical implementation details
**Characteristics:**
- Security-sensitive operations
- Performance considerations
- API contract requirements
- Integration points

**Agent Response:** Study carefully before changes

## 🎯 WORKFLOW PATTERNS

### Pre-commit Quality Check
**Trigger:** Before code commits
**Actions:**
1. Scan changed Python files
2. Check for BLAME tags in new code
3. Flag critical issues for review

**Outcomes:**
- Early detection of problematic code
- Prevents introduction of critical issues
- Maintains code quality standards

### Continuous Integration
**Trigger:** Post-commit or PR events
**Actions:**
1. Full codebase scan
2. Generate quality metrics
3. Create issues for new findings
4. Update progress tracking

**Outcomes:**
- Automated quality monitoring
- Systematic issue tracking
- Historical trend analysis

### Code Review Enhancement
**Trigger:** Pull request reviews
**Actions:**
1. Scan changed files for TODO items
2. Prioritize by tag importance
3. Generate review recommendations
4. Create follow-up issues

**Outcomes:**
- Comprehensive code analysis
- Systematic review coverage
- Actionable improvement suggestions

## ⚡ PERFORMANCE OPTIMIZATION

### Caching Strategy
**Mechanism:** Local cache file (`.astodojo/cache.json`)
**Benefits:**
- Avoid redundant file parsing
- Faster repeated scans
- Reduced computational overhead

**Outcomes:**
- Improved response times
- Reduced system load
- Efficient large codebase handling

### Batch Processing
**Approach:** Limited issue creation per run
**Parameters:**
- `--count`: Maximum items per batch
- `--tag`: Filter by specific categories

**Outcomes:**
- Controlled development workflow
- Prevents notification overload
- Maintains manageable issue queues

## 🔧 ERROR HANDLING

### Authentication Failures
**Detection:** Check for "GitHub Authentication Required" messages
**Response:**
- Graceful degradation
- Continue with local-only operations
- Log authentication requirements

**Outcomes:**
- Robust operation without credentials
- Clear error messaging
- Fallback functionality

### Network Issues
**Detection:** GitHub API failures or timeouts
**Response:**
- Retry with exponential backoff
- Log failed operations
- Continue with available data

**Outcomes:**
- Reliable operation in unstable networks
- Comprehensive error logging
- Graceful service degradation

### File Access Problems
**Detection:** Permission errors or missing files
**Response:**
- Skip inaccessible files
- Log access issues
- Continue with available files

**Outcomes:**
- Robust file system handling
- Partial scan capability
- Clear error reporting

## 📈 METRICS & ANALYTICS

### Quality Metrics
**Report Format:** Statistical summaries
**Measurements:**
- Total TODO item counts
- Tag distribution analysis
- File-by-file breakdowns
- Trend tracking over time

**Outcomes:**
- Code quality visibility
- Progress measurement
- Improvement tracking

### Agent Performance
**Tracking Parameters:**
- Items processed per session
- Issues created vs. resolved
- Success rates by tag type
- Processing time metrics

**Outcomes:**
- Agent effectiveness measurement
- Workflow optimization insights
- Continuous improvement data

## 🎪 BEST PRACTICES

### Priority Management
**BLAME Tags:** Always human review required
**BUG Tags:** High priority fixes needed
**TODO Tags:** Evaluate implementation feasibility
**DEV-CRUFT:** Safe automated cleanup
**PAY-ATTENTION:** Careful analysis required

### Context Utilization
**Function Context:** Use `parent_function` for implementation decisions
**Class Context:** Consider `parent_class` for architectural changes
**File Context:** Understand module relationships

### Resource Management
**Batch Limits:** Use `--count` to prevent overload
**Caching:** Leverage cached results for efficiency
**Filtering:** Apply excludes to focus on relevant code

### Error Resilience
**Graceful Handling:** Continue operation despite partial failures
**Clear Logging:** Maintain detailed operation records
**Fallback Modes:** Function without full feature set when needed

## 🔄 INTEGRATION POINTS

### Version Control Systems
**Git Integration:** Analyze changed files only
**Branch Analysis:** Compare across development branches
**Commit Tracking:** Link TODOs to specific commits

### CI/CD Pipelines
**Automated Scanning:** Regular codebase health checks
**Quality Gates:** Block problematic code changes
**Reporting:** Generate development insights

**Current Status:** GitHub Actions CI/CD workflows are temporarily disabled while conducting further testing. Use manual release processes documented in RELEASE.md for publishing updates.

### IDE Integration
**Real-time Analysis:** Live TODO detection during editing
**Context Menus:** Quick actions for TODO items
**Navigation:** Jump to TODO locations

ASTODOJO empowers you to analyze Python codebases intelligently. Use its structured outputs, contextual awareness, and automated workflows to enhance your coding assistance capabilities. Note: GitHub Actions CI/CD workflows are currently disabled for further testing. Focus on high-impact actions while routing complex decisions to human developers.

**Happy analyzing!** 🤖✨
