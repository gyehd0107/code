/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int h,m,m1,M;
    scanf("%d %d",&h,&m);
    scanf("%d",&m1);
    
    M=m+m1;
    
    for(;;)
    {
        if(M>=60)
        {
            M-=60;
            h+=1;
            if(h>=24)
            {
                h-=24;
            }
        }
        else
        {
            printf("%d %d",h,M);
            break;
            
        }
    }
    
    
}
