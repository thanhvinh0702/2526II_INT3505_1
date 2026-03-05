package com.hoangvinh.bai2.mappers;

import com.hoangvinh.bai2.dto.UserResponse;
import com.hoangvinh.bai2.model.User;
import org.springframework.stereotype.Component;

@Component
public class UserMapper {

    public UserResponse toResponse(User user) {
        return UserResponse.builder()
                .id(user.getId())
                .email(user.getEmail())
                .username(user.getUsername())
                .build();
    }
}
