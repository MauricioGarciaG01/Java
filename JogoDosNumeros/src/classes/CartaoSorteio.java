/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package classes;
import java.util.Random;

public class CartaoSorteio extends Cartao{

    
    public CartaoSorteio() {
        super(6);
        
    }
    
    public void sorteiaNumeros(){
        Random sorteio = new Random();
        
        while(getTotNumeros()<=6){
            int numero = sorteio.nextInt(50)+1;
            addNumeros(numero);
        }
    }
    
    
    
    
    
    
    
}
