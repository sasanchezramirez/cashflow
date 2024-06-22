# Usa una imagen base de Node.js
FROM node:22-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el código de la aplicación
COPY . .

# Construye la aplicación para producción
RUN npm run build --prod

# Usa una imagen base de Nginx para servir la aplicación
FROM nginx:alpine

# Copia los archivos construidos de Angular al directorio de Nginx
COPY --from=0 /app/dist/cashflow-front /usr/share/nginx/html

# Expone el puerto en el que correrá Nginx
EXPOSE 80

# Comando para correr Nginx
CMD ["nginx", "-g", "daemon off;"]
