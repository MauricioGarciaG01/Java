
package classes;

public class CartaoAposta extends Cartao{
    
    private static int numeroAposta;
    
    
    public CartaoAposta(int qtdNumeros){
        super(qtdNumeros);
        setNumeroAposta();
    }

    public  int getNumeroAposta() {
        return numeroAposta;
    }
    
    
    private void setNumeroAposta(){
        numeroAposta++;
    }

    public float calculaAposta(){
        int nJogados = getTotNumeros();
        float valorAposta=0;
        switch(nJogados){
            case 6:
                valorAposta = 4.5f;
                break;
            case 7:
                valorAposta = 31.5f;
                break; 
            case 8:
                valorAposta = 126;
                break;
            case 9:
                valorAposta = 378;
                break;
            case 10:
                valorAposta = 945;
                break;
        }
        return valorAposta;
    }
    
}
