// ==========================================
// Esquema de Base de Datos Relacional Local
// Canal Marketplace - Prisma ORM (PostgreSQL 16)
// ==========================================

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

/// Estado temporal del carrito de compras (visitantes anónimos y clientes autenticados)
/// Épica: EP-ITC | Historia de Usuario: HU-ITC-CAR, HU-ITC-RES
model CartItem {
  id          String   @id @default(uuid())
  sessionId   String?  // Identificador de sesión para usuarios anónimos
  customerId  String?  // ID del cliente autenticado (asociado tras login)
  productId   String   // ID referencial de la variante de producto (Módulo Productos)
  quantity    Int      @default(1)
  unitPrice   Decimal  @db.Decimal(10, 2)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  @@index([sessionId])
  @@index([customerId])
  @@map("cart_items")
}

/// Lista de favoritos persistente asociada exclusivamente al ID del cliente
/// Épica: EP-ITC | Historia de Usuario: HU-ITC-FAV
model WishlistItem {
  id         String   @id @default(uuid())
  customerId String   // ID del cliente autenticado (Módulo Seguridad)
  productId  String   // ID del producto/variante guardado (Módulo Productos)
  createdAt  DateTime @default(now())

  @@unique([customerId, productId]) // Evita duplicar el mismo favorito por cliente
  @@index([customerId])
  @@map("wishlist_items")
}
