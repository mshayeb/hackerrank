// https://www.hackerrank.com/challenges/n-puzzle

#include <stdio.h>
#include <stdlib.h>

int MisMatch(char **board, int N){
		int won = 1,i,j,count=0,x=0;
		for(i=0;i<N;i++){
			for(j=0;j<N;j++){
				if(board[i][j] != count){
					won=0;break;}
			}
			if(won == 0)
				break;
		}
		return won;
}

int main(){
	
	int N,i,j;
	scanf("%d",&N);
	char **board = malloc(N*sizeof(char*));
	for(i=0;i<N;i++){
		board[i] = malloc(N*sizeof(char));
		for(j=0;j<N;j++){
			scanf("%c\n",&board[i][j]);
		}
	}
}