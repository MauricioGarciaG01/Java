/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Classes;

import java.util.ArrayList;
import java.util.Random;

/**
 *
 * @author Keslley
 */
public class JogoDaForca {
    private String palavra;
    private ArrayList<Palavras> palavras;
    private ArrayList<Character> acertos;
    private ArrayList<Character> erros;
    private ArrayList<Character> usadas = new ArrayList <>();

    
    private int num;
    private String sorteada;
    private int totErros;
    
     public JogoDaForca() {
        this.palavras = new ArrayList<>();
        adicionaPalavras();
    }
    
    public void somadosErros(){
        this.totErros++;
    }
    
    public void setUsadas(char letra) {
        this.usadas.add(letra);
    }

    public ArrayList<Palavras> getPalavras() {
        return palavras;
    }

    public void setPalavras(ArrayList<Palavras> palavras) {
        this.palavras = palavras;
    }

    public ArrayList<Character> getAcertos() {
        return acertos;
    }

    public void setAcertos(ArrayList<Character> acertos) {
        this.acertos = acertos;
    }

    public ArrayList<Character> getErros() {
        return erros;
    }

    public void setErros(ArrayList<Character> erros) {
        this.erros = erros;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public String getSorteada() {
        return sorteada;
    }

    public void setSorteada(String sorteada) {
        this.sorteada = sorteada;
    }

    public int getTotErros() {
        return totErros;
    }

    public void setTotErros(int totErros) {
        this.totErros = totErros;
    }
   
    private void adicionaPalavras(){
        palavras.add(new Palavras("CARRO", "QUATRO RODAS"));
        palavras.add(new Palavras("MOTO", "DUAS RODAS"));
        palavras.add(new Palavras("LOJA", "VENDEDOR"));
        palavras.add(new Palavras("CAMINHÃO", "EIXOS"));
        palavras.add(new Palavras("BIBLIOTECA", "LEITURA"));
        palavras.add(new Palavras("LIVROS", "CONHECIMENTO"));
        palavras.add(new Palavras("ESTRADA", "CAMINHO"));
        palavras.add(new Palavras("LIXO", "RECICLAVEL"));
        palavras.add(new Palavras("CONTROLE", "BOTÕES"));
        palavras.add(new Palavras("ESCOLA", "ESTUDANTE"));
        
    }
    
    public String sorteiaPalavras(){
        Random rand = new Random();
        
        num = rand.nextInt(palavras.size());
   
        return palavras.get(num).getPalavra();
    }//Exception, IOException, SQLException sao exceçoes que precisam ser tratados
    
    
    public String retornaPalavras() throws NullPointerException{
        
        try{
            switch (palavras.get(num).getPalavra()) {
                case "CARRO":
                    palavras.get(0).getPalavra();
                    break;
                case "MOTO":
                    palavras.get(1).getPalavra();
                    break;
                case "LOJA":
                    palavras.get(2).getPalavra();
                    break;
                case "CAMINHÃO":
                    palavras.get(3).getPalavra();
                    break;
                case "BIBLIOTECA":
                    palavras.get(4).getPalavra();
                    break;
                case "LIVROS":
                    palavras.get(5).getPalavra();
                    break;
                case "ESTRADA":
                    palavras.get(6).getPalavra();
                    break;
                case "LIXO":
                    palavras.get(7).getPalavra();
                    break;
                case "CONTROLE":
                    palavras.get(8).getPalavra();
                    break;
                case "ESCOLA":
                    palavras.get(9).getPalavra();
                    break;
            }
        }catch(Exception ex){
            throw new NullPointerException();
        }       
            return palavras.get(num).getPalavra();
    }
    
    public void inicioJogo(){
        //sorteada = retornaPalavras();
        palavra = sorteiaPalavras();
        acertos = new ArrayList<>();
        erros = new ArrayList<>();
        
        for(int i = 0; i < palavra.length();i++){
            acertos.add('_');
        }
        
    }
    
    public String retornaDicas() throws NullPointerException{
        
        try{
            switch (palavras.get(num).getDica()) {
                case "CARRO":
                    palavras.get(0).getDica();
                    break;
                case "MOTO":
                    palavras.get(1).getDica();
                    break;
                case "LOJA":
                    palavras.get(2).getDica();
                    break;
                case "CAMINHÃO":
                    palavras.get(3).getDica();
                    break;
                case "BIBLIOTECA":
                    palavras.get(4).getDica();
                    break;
                case "LIVROS":
                    palavras.get(5).getDica();
                    break;
                case "ESTRADA":
                    palavras.get(6).getDica();
                    break;
                case "LIXO":
                    palavras.get(7).getDica();
                    break;
                case "CONTROLE":
                    palavras.get(8).getDica();
                    break;
                case "ESCOLA":
                    palavras.get(9).getDica();
                    break;
            }
        }catch(Exception ex){
            throw new NullPointerException("Digite uma letra!");
        }        
            return palavras.get(num).getDica();
    }
    
    public boolean encontrou(char letra){
        boolean nExiste = false;
        sorteada = retornaPalavras();
        
        for(int i = 0; i< sorteada.length(); i++){
            if(sorteada.charAt(i) == letra){
                nExiste = true;
                acertos.set(i, letra);   
            }
        }
        if(!nExiste){
            erros.add(letra);
            return false;
        }
        return true;
    }
    
    public boolean jogoAcabado(){
        return ganhastes() || perdestes();
    }
    
    public boolean ganhastes(){
        return !acertos.contains('_');
    }
    
    public boolean perdestes(){
        return totErros == 7;
    }
    
    public String letraSorteada(char letra){
        sorteada = retornaPalavras();
       
        StringBuilder saida = new StringBuilder(); 
        for(int i =0; i < sorteada.length(); i++){
            if(letra == sorteada.charAt(i)){
                saida.append(letra).append("-");
            }
        }
        return saida.toString();
    }
    
    
    public String letrasUsadas(){
        StringBuilder saida = new StringBuilder();
        
        for(int i=0; i < usadas.size();i++){
            saida.append(usadas.get(i)).append("  ");
        }
        return saida.toString();
 
    }
    
    
    public String exibiAcertos(){
        StringBuilder saida = new StringBuilder();
        
        for(int i=0; i < acertos.size();i++){
            saida.append(acertos.get(i)).append("  ");
        }
        return saida.toString();
    }
    
    public String exibiErradas(){
         StringBuilder saida = new StringBuilder();
        
        for(int i=0; i < erros.size();i++){
            saida.append(erros.get(i)).append("  ");
        }
        return saida.toString();
    }
    
}
