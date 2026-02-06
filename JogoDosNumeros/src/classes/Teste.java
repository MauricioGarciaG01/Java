/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package classes;

public class Teste {

    
    public static void main(String[] args) {
        CartaoAposta teste = new CartaoAposta(6);
        
        System.out.print("Primeira aposta"+teste.getNumeroAposta());
        teste = new CartaoAposta(7);
        System.out.print("Segunda aposta"+teste.getNumeroAposta());
    }
    
}
