from tiktoken import count_tokens

class OpenAICostCalculator:

    @classmethod
    def __count_openai_tokens(cls, text):
        '''counts tokens with openai'''
        return count_tokens(text)

    @classmethod
    def input_cost(cls, user_input, rate):
        '''cost of tokens for user input'''
        token_count = cls.__count_openai_tokens(user_input)
        return token_count * rate

    @classmethod
    def output_cost(cls, ai_output, rate):
        '''cost of tokens for ai output'''
        token_count = cls.__count_openai_tokens(ai_output)
        return token_count * rate
