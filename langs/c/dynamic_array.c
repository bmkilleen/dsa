/**
 * @file dynamic_array.c
 *
 * @brief Automatically resiszing array
 *
 * TODO:
 *
 */

#ifndef DYNAMIC_ARRAY_H
#define DYNAMIC_ARRAY_H

// Value to be stored in the array.
typedef void *DynamicArrayElement;

typedef struct _DynamicArray DynamicArray;

struct _DynamicArray
{
    DynamicArrayElement *data;
    unsigned int length;
    unsigned int _alloced;
};

/**
 * Compare two elements of the array.
 */
typedef int (*DynamicArrayEqualFunc)()
