# Agents for Amazon Bedrock Test UI

A generic Streamlit UI for testing generative AI agents built using Agents for Amazon Bedrock. For more information, refer to the blog post [Developing a Generic Streamlit UI to Test Amazon Bedrock Agents](https://blog.avangards.io/developing-a-generic-streamlit-ui-to-test-amazon-bedrock-agents).

# Prequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Python 3](https://www.python.org/downloads/)

# Running Locally
1. Create an environment.
   ```
   python -m venv <environment-name>
   ```
2. Activate the environment. (In Windows)

   ```
   .\<environment-name>\Scripts\activate.ps1
   ```

3. Run the following `pip` command to install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set the following environment variables:
   - `BEDROCK_AGENT_ID` - The ID of the agent
   - `BEDROCK_AGENT_ALIAS_ID` - The ID of the agent alias. The default `TSTALIASID` will be used if it is not set.
   - The [AWS environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) that provides the credentials to your account. The principal must have the necessary permissions to invoke the Bedrock agent.
```
SET BEDROCK_AGENT_ID=WENOOVMMEK
SET BEDROCK_AGENT_TEST_UI_TITLE="InvestRock - Mutual Fund AI assistant\n Welcome to InvestRock! Would you like to explore our list of mutual funds, or do you have specific investment goals in mind for creating a diversified portfolio? I am a helpful chat assistant. How can I help you?"
```
5. (Optional) Set the following environment variables to customize the UI:
   - `BEDROCK_AGENT_TEST_UI_TITLE` - The page title. The default `Agents for Amazon Bedrock Test UI` will be used if not set.
   - `BEDROCK_AGENT_TEST_UI_ICON` - The favicon, such as `:bar_chart:`. The default Streamlit icon will be used if it is not set.
6. Run the following command to start the Streamlit app:

   ```
   streamlit run app.py --server.port=8080 --server.address=localhost
   ```
