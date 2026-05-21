import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

export async function getUserByEmail(emailAddress: string) {
  return prisma.user.findFirst({
    where: { emailAddress: emailAddress },
    select: { id: true, emailAddress: true, name: true },
  });
}
