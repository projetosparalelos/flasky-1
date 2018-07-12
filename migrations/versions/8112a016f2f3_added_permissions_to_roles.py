"""added permissions to roles

Revision ID: 8112a016f2f3
Revises: 617c2484a85f
Create Date: 2018-07-12 17:10:29.110074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8112a016f2f3'
down_revision = '617c2484a85f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
