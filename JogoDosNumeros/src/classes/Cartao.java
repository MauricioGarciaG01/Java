package classes;

public class Cartao {

    private int numeros[];
    private int totNumeros;

    public Cartao(int totNumeros) {
        numeros = new int[totNumeros];
    }

    public int[] getNumeros() {
        return numeros;
    }

    public int getTotNumeros() {
        return totNumeros;
    }

    //Métodos gerais
    public int addNumeros(int numero) {
        if (totNumeros < numeros.length) {
            if (!existe(numero)) {
                numeros[totNumeros++] = numero;
                return 1;//adicionou com sucesso
            } else {
                return 0;//o elemento já existe.
            }
        }
        return 2;//estouro de memória.
    }

    public boolean existe(int numeroProcurado) {
        for (int i = 0; i < totNumeros; i++) {
            if (numeroProcurado == numeros[i]) {
                return true;
            }
        }
        return false;
    }

    public String numerosCartao() {

        StringBuilder saida = new StringBuilder();
        for (int i = 0; i < totNumeros; i++) {
            saida.append(numeros[i]).append("\t");
        }

        return saida.toString();
    }

}
