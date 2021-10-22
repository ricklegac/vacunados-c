#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct vacunados{
	char nombre[30];
	char apellido[30];
	char establecimiento[30];
	char fecha[20];
	int ci;
	int dosis;
	char descripcion[40];
	char actualizacion[20];
}personas;
int main(){
	FILE *fp=fopen("vacunados.csv","r");
	if(fp==NULL){
		perror("no se pudo abrir.");
		exit(1);
	}
	personas valores;
	char buffer[1024];
	int k=0;
	int contador_filas=0,contador_columnas=0,menores=0,primeradosis=0,segundadosis=0,otrasdosis=0;
	int i=0,n=0,contador=0;
	int pfizer=0,moderna=0,astrazeneca=0,sputnik=0,hayat=0,otros=0,sinopharm=0,covaxin=0,coronovac=0;
	char vacunas[8][40]={
		"PFIZER - COVID -19",
		"ASTRAZENECA-CHADOX1-S - COVID-19",
		"MODERNA - COVID -19",
		"HAYAT VAX COVID-19",
		"SPUTNIK V COVID-19",
		"SINOPHARM COVID-19",
		"COVAXIN COVID-19",
		"CORONAVAC COVID-19"

	};//un array bidimensional donde en cada fila guardare las vacunas diferentes
	while(fgets(buffer,1024,fp)){
		//printf("%s\n",buffer);
		contador_columnas=0;
		contador_filas++;
		char *field = strtok(buffer,";"); //estan separadas por ; en el archivo original
		if(contador_filas==1)
			continue; //aca pasamos de largo cuando lee el titulo del csv
		
		while(field){
			if(contador_columnas==0){
				strcpy(valores.nombre,field);
				if(strcmp(valores.nombre,"MENOR DE EDAD")==0){
					menores++;
				}
			}
			if(contador_columnas==6){
				if(strcmp(field,vacunas[0])==0)
					pfizer++;
				else if(strcmp(field,vacunas[1])==0)
					astrazeneca++;
				else if(strcmp(field,vacunas[2])==0)
					moderna++;
				else if(strcmp(field,vacunas[3])==0)
					hayat++;
				else if(strcmp(field,vacunas[4])==0)
					sputnik++;
				else if(strcmp(field,vacunas[5])==0)
					sinopharm++;
				else if(strcmp(field,vacunas[6])==0)
					covaxin++;
				else if(strcmp(field,vacunas[7])==0)
					coronovac++;

			}
			if(contador_columnas==5){
				valores.dosis = *field-'0';
				if(valores.dosis==1){
					primeradosis++;
				}else if(valores.dosis==2){
					segundadosis++;
				}else{
					otrasdosis++;
				}

			}
			field=strtok(NULL,";"); //actualizamos el valor de la columna
			contador_columnas++;
		}
		i++;
	}
	int distribucion[8]={pfizer,astrazeneca,moderna,hayat,sputnik,sinopharm,covaxin,coronovac};
	fclose(fp);
	printf("cantidad de personas vacunadas: %d\n",contador_filas-1);
	printf("cantidad de personas menores de edad: %d\n",menores);
	printf("cantidad de personas con primera dosis: %d\n",primeradosis);
	printf("cantidad de personas con segunda dosis: %d\n",segundadosis);
	printf("cantidad de personas con otras dosis: %d\n",otrasdosis);
	printf("---------------------------------------------------\nDOSIS\t\t\t\t CANTIDAD\n");
	for(i=0;i<8;i++){
		printf("%s: \t\t\t%d\n",vacunas[i],distribucion[i]);
	}
	return 0;
}
