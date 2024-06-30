# Usa una imagen base de Node.js
FROM node:22-alpine

# Establece el directorio de trabajo
WORKDIR /cashflow-front

# Copia el archivo package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el código de la aplicación
COPY . .

# Construye la aplicación para producción
RUN npm run build 
# Usa una imagen base de Nginx para servir la aplicación
FROM nginx:alpine

# # Elimina los archivos por defecto de Nginx
# RUN rm -rf /usr/share/nginx/html/*

# Copia los archivos construidos de Angular al directorio de Nginx
COPY --from=0 /cashflow-front/dist/cashflow-front /usr/share/nginx/html

# Listar archivos en el directorio de Nginx para depuración
RUN ls -la /usr/share/nginx/html

# Expone el puerto en el que correrá Nginx
EXPOSE 80

# Comando para correr Nginx
CMD ["nginx", "-g", "daemon off;"]
