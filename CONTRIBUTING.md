# Contributing Guidelines
Thank you for considering contributing to this project! To maintain a clean and efficient workflow, please follow these guidelines when naming branches and structuring your commit messages.

## Branch Naming Conventions
Branch names should be descriptive and follow a consistent naming convention. This helps in understanding the purpose of the branch and ensures that multiple contributors can work without conflicts.

### Format
    <type>/<issue-number>-<short-description>

### Types
-   **feature**: New features or enhancements.
-   **bugfix**: Fixes for bugs or issues.
-   **hotfix**: Urgent fixes that need to be applied directly to the `main` branch.
-   **refactor**: Code refactoring without changing functionality.
-   **docs**: Changes or additions to documentation.
-   **test**: Adding or modifying tests.
-   **chore**: Routine tasks like updating dependencies.

### Examples
-   `feature/23-user-authentication`
-   `bugfix/45-fix-login-error`
-   `docs/50-update-readme`
-   `refactor/35-optimize-db-queries`
-   `test/42-add-coverage-for-login`

## Commit Message Structure
Commit messages should be clear and concise. Properly formatted commit messages help in understanding the history of the project and make it easier to track changes.

### Format
    <type>(<scope>): <short-description> <body>
### Types
-   **feat**: A new feature.
-   **fix**: A bug fix.
-   **docs**: Documentation changes.
-   **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.).
-   **refactor**: A code change that neither fixes a bug nor adds a feature.
-   **perf**: A code change that improves performance.
-   **test**: Adding missing tests or correcting existing tests.
-   **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation.

### Scope
-   The `scope` is optional but recommended. It refers to the part of the codebase affected by the commit (e.g., `auth`, `api`, `ui`, `db`). If your commit affects multiple scopes, you can use a general term like `core`.

### Description
-   Use the imperative, present tense ("change" not "changed" or "changes") to describe what the commit does.

### Body
-   The body is optional but should be used to provide additional context about the commit. Explain _why_ the change was made and _how_ it addresses the issue.

### Examples
-   **Simple Commit**:
`feat(api): add user authentication endpoint`

- **Detailed Commit**:
`fix(auth): resolve token expiration issue`
`The token was expiring too early due to incorrect time zone handling. Updated the expiration logic to use UTC consistently across the application.`

## Pull Request Guidelines
1.  **Branch from `main`**: Always create a new branch from the `main` branch for your work.
2.  **Descriptive Pull Requests**: Include a clear description of what your changes do, why they are necessary, and any additional context that reviewers might need.
3.  **Link Issues**: If your pull request addresses an open issue, link to the issue in the pull request description.
4.  **Review Process**: Be responsive to review comments. Address the feedback by updating your branch and notifying the reviewer.
5.  **Keep Commits Clean**: Squash commits when possible to maintain a clean and readable history. Use interactive rebase (`git rebase -i`) to combine multiple commits that serve the same purpose.

## Testing
1.  **Write Tests**: If you add a new feature or fix a bug, write tests to cover the new or changed functionality.
2.  **Run Tests**: Ensure that all tests pass before pushing your changes. This includes any existing tests that might be affected by your changes.
3.  **Automated Testing**: If the project uses continuous integration, make sure your code passes all automated checks before requesting a merge.

## Code Style
1.  **Follow the Style Guide**: Adhere to the project's coding standards and style guide. If no guide exists, follow PEP 8.
2.  **Linting**: Run linter`flake8` to ensure code quality before committing.
3.  **Comments**: Write meaningful comments, especially for complex or non-obvious code sections. Use comments to explain why something is done, not just what is done.

## Documentation
1.  **Update Documentation**: Ensure that relevant documentation is updated to reflect your changes. This includes README files, inline code comments, and any API documentation.
2.  **Document New Features**: When adding new features, include usage examples, explanations, and any necessary setup instructions.

## Conclusion
Following these guidelines will help us maintain a high-quality codebase and ensure that collaboration is smooth and efficient. Thank you for contributing!
