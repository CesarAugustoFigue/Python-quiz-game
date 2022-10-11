from unittest import TestCase, main
import Quiz
import opcoes

def eh_string_fn(val: str) -> bool:
    if isinstance(val, str):
        return True
    else:
        return False

def eh_int_fn(val: int) -> bool:
    if isinstance(val, int):
        return True
    else:
        return False 

class TestesQuiz(TestCase):

    #testes para password
    def test_senha_fn(self):
        self.assertNotEquals(Quiz.senha_req, '')

    def test_senha_fn_valida(self):
        self.assertIsNot(Quiz.senha, '')

    def test_senha_fn_type(self):
        self.assertEqual(eh_string_fn(Quiz.senha_req), True)


    #testes para user        
    def test_usuario_fn(self):
        self.assertNotEquals(Quiz.usuario, '')

    def test_usuario_fn_valido(self):
        self.assertIsNot(Quiz.usuario, '')

    def test_usuario_fn_type(self):
        self.assertEqual(eh_string_fn(Quiz.usuario), True)


    #testes para o program quiz
    def test_usuario_fn_type(self):
        self.assertEqual(eh_string_fn(Quiz.usuario), True)
    

if __name__ == '__main__':
    main()