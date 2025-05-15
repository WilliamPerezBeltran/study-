import { Router } from 'express';
import { UserController } from '../controllers/user.controller';

const router = Router();

// Definir las rutas
router.get('/users', UserController.getAll);
router.get('/users/:id', UserController.getById);
router.post('/users', UserController.create);
router.put('/users/:id', UserController.update);
router.delete('/users/:id', UserController.delete);


export default router;

