package org.example;

import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.KeyDeserializer;

import java.io.IOException;

public class ResidentDeserializer extends KeyDeserializer {

    @Override
    public Object deserializeKey(String s, DeserializationContext deserializationContext) throws IOException {
        return new Resident(s);
    }
}
