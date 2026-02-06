/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utilit;

/**
 *
 * @author Alinda
 */
public class Utilit {
    public static String removeMasc(String campo) {
        String campoAux = campo.replace(".", "");
        campoAux = campoAux.replace("-", "");
        campoAux = campoAux.replace("/", "");
        campoAux = campoAux.replace("(", "");
        campoAux = campoAux.replace(")", "");
        campoAux = campoAux.replace(",", "");
        campoAux = campoAux.replace("_", "");
        campoAux = campoAux.replace(":", "");

        return campoAux;
    }
}
