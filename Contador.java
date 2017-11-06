package contador;

public class Contador {
    static int cont = 0;
    
    public int contar(){
        while (cont != 9999999){
            cont++;           
        }
        return cont;
    }
    
    
}
