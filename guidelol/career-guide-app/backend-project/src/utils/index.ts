export const log = (message: string): void => {
    console.log(message);
};

export const validateEmail = (email: string): boolean => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
};

export const generateId = (): string => {
    return Math.random().toString(36).substr(2, 9);
};