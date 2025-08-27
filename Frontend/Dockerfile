FROM node:24-alpine

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .

EXPOSE 5173

# 7️⃣ Start Vite dev server
CMD ["npm", "run", "dev"]
